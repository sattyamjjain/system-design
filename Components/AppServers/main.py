from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, world!'})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
