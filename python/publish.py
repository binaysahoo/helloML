import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379)

# Publish messages to a channel
r.publish('mychannel', 'Hello subscribers!')
r.publish('mychannel', 'How are you?')

