from confluent_kafka import Consumer, Producer, admin
from distribuidos_common import Cassandra
from itertools import cycle
import fastavro
import logging
import io
import math 
import os

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s.%(funcName)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
SERVER = os.getenv("KAFKA_HOST")
GROUP_ID = os.getenv("GROUP_ID")

CONSUMER_CONFIG = {
    'bootstrap.servers': SERVER,
    'group.id': GROUP_ID
}
CONSUMER_CONFIG2 = {
    'bootstrap.servers': SERVER
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
        return None 
    

def magnitude_correction2(magpsf, sigmapsf, magnr, sigmagnr, isdiffpos):
    if(isdiffpos == 't'):
        return (pow( pow(10,-0.8*float(magpsf))*float(sigmapsf**2)*(pow(-10,float(magnr))*float(sigmagnr)**2),0.5))/(pow(10,-0.4*float(magnr))+(pow(10,0.4*float(magpsf))))
    else:
        return (pow( pow(10,-0.8*float(magpsf))*float(sigmapsf**2)*(pow(-10,float(magnr))*float(sigmagnr)**2),0.5))/(pow(10,-0.4*float(magnr))-(pow(10,0.4*float(magpsf))))


def insert(objectid,fid,magpsf, sigmapsf, magpsf_corr,sigmapsf_corr,jd):
    c = Cassandra.getInstance()
    c.execute(
    """
    INSERT INTO pipeline.deteccion (objectid, id, info)
    VALUES ( %d , %s , %s);
    """,
    VALUES (objectid, uuid(), {'fid': fid, 'magpsf': magpsf, 'sigmapsf': sigmapsf, 'magpsf_corr': magpsf_corr, 'sigmapsf_corr': sigmapsf_corr, 'jd': jd});
    print("funciona")
)



consumer = Consumer(CONSUMER_CONFIG)
last_topic = list_topics(consumer)
logging.info(f"Subscribed to {last_topic}")
consumer.subscribe(last_topic)
producer = Producer(CONSUMER_CONFIG2)
particion = cycle(range(4))
while True:
    msg = consumer.poll(timeout=10)
    if msg:
        data = get_message(msg)
        logging.info(f"Consuming {data['objectId']} - {data['candidate']['jd']}")
        magpsf_corr = magnitude_correction(data['candidate']['magnr'],data['candidate']['isdiffpos'],data['candidate']['magpsf'])
        sigmapsf_corr = magnitude_correction2(data['candidate']['magpsf'],data['candidate']['sigmapsf'],data['candidate']['magnr'],data['candidate']['sigmagnr'],data['candidate']['isdiffpos'])
        insert(data['candidate']['objectid'], data['candidate']['fid'],data['candidate']['magnr'], data['candidate']['sigmapsf'], magpsf_corr, sigmapsf_corr, data['candidate']['jd'] )
        producer.produce('Calculo', value=data['objectId'], particion = next(particion))
        producer.flush()
    else:
    	logging.info(f"Error {msg}")
    	last_topic = list_topics(consumer)
    	consumer.subscribe([last_topic])