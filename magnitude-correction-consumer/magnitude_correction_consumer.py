from confluent_kafka import Consumer
from distribuidos_common import Cassandra
import fastavro
import logging
import io
import math 
from uuid import uuid4

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s.%(funcName)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

CONSUMER_CONFIG = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'testo'
}


def list_topics(c: Consumer , filter_by="ztf"):
    topics = c.list_topics().topics.keys()
    return list(filter(lambda x: filter_by in x, list(topics)))


def get_message(message):
    bytes_io = io.BytesIO(message.value())
    reader = fastavro.reader(bytes_io)
    return reader.next()

def magnitude_correction(magnr,isdiffpos,magpsf):
    if(isdiffpos == 't'):
        return -2.5*math.log(pow(10,-0.4*float(magnr))+(pow(10,0.4*float(magpsf))),10) 
    else:
        return 0 
    

def magnitude_correction2(magpsf, sigmapsf, magnr, sigmagnr, isdiffpos):
    if(isdiffpos == 't'):
        result =  (pow( pow(10,-0.8*float(magpsf))*float(sigmapsf**2)*(pow(-10,float(magnr))*float(sigmagnr)**2),0.5))/(pow(10,-0.4*float(magnr))+(pow(10,0.4*float(magpsf))))
    else:
        result =  (pow( pow(10,-0.8*float(magpsf))*float(sigmapsf**2)*(pow(-10,float(magnr))*float(sigmagnr)**2),0.5))/(pow(10,-0.4*float(magnr))-(pow(10,0.4*float(magpsf))))
    if(isinstance(result, complex)):
        return 0
    return result

def insert(objectid,fid,magpsf, sigmapsf, magpsf_corr,sigmapsf_corr,jd, c ):
    
    c.execute(
    '''
    INSERT INTO pipeline2.deteccion (objectid, id, info)
    VALUES ( %s , %s , %s);
    ''',
    (objectid, uuid4(), {'fid': fid, 'magpsf': magpsf, 'sigmapsf': sigmapsf, 'magpsf_corr': magpsf_corr, 'sigmapsf_corr': sigmapsf_corr, 'jd': jd})
)



consumer = Consumer(CONSUMER_CONFIG)
last_topic = list_topics(consumer)
logging.info(f"Subscribed to {last_topic}")
consumer.subscribe(last_topic)
c = Cassandra.getInstance()
while True:
    msg = consumer.poll(timeout=10)
    if msg:
        data = get_message(msg)
        logging.info(f"Consuming {data['objectId']} - {data['candidate']['jd']}")
        magpsf_corr = magnitude_correction(data['candidate']['magnr'],data['candidate']['isdiffpos'],data['candidate']['magpsf'])
        sigmapsf_corr = magnitude_correction2(data['candidate']['magpsf'],data['candidate']['sigmapsf'],data['candidate']['magnr'],data['candidate']['sigmagnr'],data['candidate']['isdiffpos'])
        insert(data['objectId'], data['candidate']['fid'],data['candidate']['magnr'], data['candidate']['sigmapsf'], magpsf_corr, sigmapsf_corr, data['candidate']['jd'],c )
    else:
    	logging.info(f"Error {msg}")
    	last_topic = list_topics(consumer)
    	consumer.subscribe([last_topic])