from flask import Flask, request
from redis import Redis
import json

app = Flask(__name__)
redis = Redis(host='localhost', port=6379)


@app.route('/message', methods=['POST'])
def add_message():
    message = json.loads(request.data)
    redis.publish('messages', json.dumps(message))
    return 'Message received'


if __name__ == '__main__':
    app.run(debug=True)
