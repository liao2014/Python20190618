# Author:UserA
# redis快速入门2——使用连接池
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

r = redis.Redis(connection_pool=pool)
r.set('name', 'UserA')
print(r.get('name'))
