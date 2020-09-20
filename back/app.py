import redis 
from flask import Flask, jsonify
from flask_cors import CORS 
import json

app = Flask(__name__)
CORS(app)
cache = redis.StrictRedis(host=, port=,db=,password=,decode_responses=True)

@app.route('/')
def keys():
    values = cache.smembers("objetos")
    '''for key in cache.scan_iter():
        values.append(key)'''
    return jsonify({'data': list(values)})

@app.route('/NB/<id>')
def nearlyBlack(id):
    data = cache.get(id + "-NB")
    return data

@app.route('/<id>',methods=['GET'])
def getData(id):
    data = cache.get(id)
    return json.loads(data)
