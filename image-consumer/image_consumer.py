from confluent_kafka import Consumer
from gcloud import storage
import cv2
import fastavro
import logging
import io
import math 
import sys
import numpy as np
import pandas as pd
import os
import gzip
import matplotlib.pyplot as plt
from PIL import Image
from astropy.io import fits
from distribuidos_common import Redis


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



def images(stamp_byte,r,name):
    with gzip.open(io.BytesIO(stamp_byte), 'rb') as f:
        with fits.open(io.BytesIO(f.read())) as hdul:
            img = hdul[0].data    
    nearlyBlack(img,r,name)
    plt.imshow(img, cmap='gray') 
    plt.savefig("img.png")
    img = cv2.imread("img.png")
    img = Image.fromarray(img)
    img.save('img.png')


def saveImg(name):
    blob = bucket.blob(name)
    with open('img.png', 'rb') as photo:
        blob.upload_from_file(photo)
    blob.make_public()
    url = blob.public_url
    print(url)

def nearlyBlack(img,r,name):
    newImg = (img.clip(0,255).astype('uint8'), 'L')
    count = 0
    count2 = 0
    for dimension1 in newImg:
        for dimension2 in dimension1:
            for dimension3 in dimension2:
                
                if(isinstance(dimension3, str)):
                    count2 = count2 + 1
                elif(dimension3 >100): 
                    count = count + 1
                    count2 = count2 + 1
    nearlyB = count/count2
    if(nearlyB > 0.6):
        r.set(name+'-NB', 'true')
    else:
        r.set(name+'-NB','false')

consumer = Consumer(CONSUMER_CONFIG)
last_topic = list_topics(consumer)
logging.info(f"Subscribed to {last_topic}")
consumer.subscribe(last_topic)
client = storage.Client()
r = Redis.getInstance()
bucket = client.get_bucket('distribuidos-astro')

while True:
    msg = consumer.poll(timeout=10)
    if msg:
        data = get_message(msg)
        logging.info(f"Consuming {data['objectId']} - {data['candidate']['jd']}")
        images(data['cutoutTemplate']['stampData'],r,data['objectId']) 
        saveImg(data['objectId'] + '/1.png')
        images(data['cutoutDifference']['stampData'],r,data['objectId']) #Diferencia entre las dos imágenes
        saveImg(data['objectId'] + '/2.png')
        images(data['cutoutScience']['stampData'],r,data['objectId']) #Del pasado
        saveImg(data['objectId'] + '/3.png')
    else:
    	logging.info(f"Error {msg}")
    	last_topic = list_topics(consumer)
    	consumer.subscribe([last_topic])