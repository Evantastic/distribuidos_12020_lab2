from distribuidos_common import Cassandra
from cassandra.util import OrderedMapSerializedKey
from estadistica import Estadistica
from json import dumps

def setup():
    Cassandra.getInstance()
    Cassandra.addQuery('SELECT info FROM deteccion WHERE objectid=?')

def addRow(dict, info):
    dict.get('magpsf_corr').append(info.get('magpsf_corr'))
    dict.get('sigmapsf_corr').append(info.get('sigmapsf_corr'))

# TODO: Crear clase estadistica e implementarla en esta funcion
def get_data(objectid):
    query = Cassandra.query(objectid)
    green = {'magpsf_corr': [], 'sigmapsf_corr': []}
    red = {'magpsf_corr': [], 'sigmapsf_corr': []}
    for rows in query:
        info = rows.info;
        if int(info.get('fid')) == 1:
            addRow(green, info)
        else:
            addRow(red, info)
    return dumps(Estadistica(green, red).__dict__)

setup()
id = 'lamejorllave';
estadistica = get_data(id)
print(estadistica)
