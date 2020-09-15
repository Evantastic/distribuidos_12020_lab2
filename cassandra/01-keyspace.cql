CREATE KEYSPACE IF NOT EXISTS pipeline WITH REPLICATION = {
    'class': 'SimpleStrategy', 'replication_factor':  1
};