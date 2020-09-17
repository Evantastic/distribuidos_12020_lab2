from distribuidos_common import Cassandra, Redis, Kafka
from cassandra.util import OrderedMapSerializedKey
from estadistica import Estadistica
from json import dumps
from sys import stdout

def setup():
    Cassandra.getInstance()
    Cassandra.addQuery('SELECT info FROM deteccion WHERE objectid=?')
    Redis.getInstance()
    Kafka.getConsumer()

def addRow(dict, info):
    dict.get('magpsf_corr').append(info.get('magpsf_corr'))
    dict.get('sigmapsf_corr').append(info.get('sigmapsf_corr'))

def get_data(objectid):
    query = Cassandra.query([objectid])
    green = {'magpsf_corr': [], 'sigmapsf_corr': []}
    red = {'magpsf_corr': [], 'sigmapsf_corr': []}
    for rows in query:
        info = rows.info;
        if int(info.get('fid')) == 1:
            addRow(green, info)
        else:
            addRow(red, info)
    return dumps(Estadistica(green, red).__dict__)

def decode(msg):
    return msg.value().decode('utf-8')

setup()
while True:
    stdout.flush()
    msg = Kafka.getConsumer().poll(1.0)
    if msg is None:
        continue
    if msg.error():
        continue
    id = decode(msg)
    estadistica = get_data(id)
    Redis.set(id, estadistica)
