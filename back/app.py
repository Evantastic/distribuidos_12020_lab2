import redis 
from flask import Flask, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)
cache = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def keys():
    values = []
    for key in cache.scan_iter():
        values.append(key)
    ids = []
    for id_data in values:
        data = cache.hgetall(id_data)
        list_aux = {
            "id": id_data,
            "nombre": data["Nombre"]
        }
        ids.append(list_aux)
    return jsonify(ids)

@app.route('/<id>',methods=['GET'])
def getData(id):
    data = cache.hgetall(id)
    return jsonify(data)
