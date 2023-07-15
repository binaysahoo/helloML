import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379)

# Subscribe to a channel
p = r.pubsub()
p.subscribe('mychannel')

# Listen for incoming messages
for message in p.listen():
    if message['type'] == 'message':
        print(message['data'].decode())

