from redis import Redis
import json

redis = Redis(host='localhost', port=6379)
pubsub = redis.pubsub()
pubsub.subscribe('messages')
for message in pubsub.listen():
    if message['type'] == 'message':
        data = json.loads(message['data'])
        print(data)
        # Do something with the message data
