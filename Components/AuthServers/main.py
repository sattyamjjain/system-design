from flask import Flask, request, jsonify
import sqlite3
import jwt

app = Flask(__name__)

JWT_SECRET_KEY = 'my-secret-key'


def generate_token(username):
    payload = {'username': username}
    return jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')


def validate_token(token):
    try:
        decoded_payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
        return decoded_payload.get('username')
    except jwt.exceptions.DecodeError:
        return None


def create_user_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username text, password text)''')
    conn.commit()
    conn.close()


def add_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()


def authenticate_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
    result = c.fetchone()
    conn.close()
    return result is not None


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if authenticate_user(username, password):
        token = generate_token(username)
        return jsonify({'token': token})
    else:
        return jsonify({'error': 'Invalid username or password'})


if __name__ == '__main__':
    app.run(debug=True)
