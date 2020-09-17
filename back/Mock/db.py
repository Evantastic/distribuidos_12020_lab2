import redis

cache = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

cache.hset(1,'Nombre','planeta1')
cache.hset(1,'Magpsf',1000)
cache.hset(1,'Sigmapsf',1000)
cache.hset(1,'Magspf_promCorr',1000)
cache.hset(1,'Magspf_desvCorr',2000)
cache.hset(1,'Sigmapsf_promCorr',1000)
cache.hset(1,'Sigmapsf_desvCorr',2000)

cache.hset(2,'Nombre','planeta2')
cache.hset(2,'Magpsf',2000)
cache.hset(2,'Sigmapsf',2000)
cache.hset(2,'Magspf_promCorr',1000)
cache.hset(2,'Magspf_desvCorr',2000)
cache.hset(2,'Sigmapsf_promCorr',2000)
cache.hset(2,'Sigmapsf_desvCorr',2000)
