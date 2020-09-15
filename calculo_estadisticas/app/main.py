from distribuidos_common import Cassandra
from cassandra.util import OrderedMapSerializedKey

c = Cassandra.getInstance()

resultado = c.execute('SELECT info FROM deteccion')

for rows in resultado:
    datos = rows.info
    fid = datos.get('fid');
    print(f'fid: {fid}')