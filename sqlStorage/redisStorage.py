from redis import StrictRedis, ConnectionPool

# redis = StrictRedis(host='localhost', port=6379, db=0)
# redis.set('name', 'Bob')
# print(redis.get('name'))

url = 'redis://localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)