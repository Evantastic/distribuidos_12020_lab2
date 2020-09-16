from distribuidos_common import Cassandra
from cassandra.util import OrderedMapSerializedKey

def setup():
    Cassandra.getInstance()
    Cassandra.addQuery('SELECT info FROM deteccion WHERE objectid=?')


// TODO: Crear clase estadistica e implementarla en esta funcion
def get_data(objectid):
    query = Cassandra.query(objectid)
    green = []
    red = []
    for rows in query:
        info = rows.info;
        if int(info.get('fid')) == 1:
            green.append(info)
        else:
            red.append(info)
    return green, red

setup()
id = 148618231249
g, r = get_data(id)
print(f'green: {g}')
print(f'red: {r}')