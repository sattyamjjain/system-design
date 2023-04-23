from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/users')
def get_users():
    name = request.args.get('name')
    age = request.args.get('age')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users"
    if name:
        query += f" WHERE name = '{name}'"
    if age:
        query += f" AND age = {age}"
    cursor.execute(query)
    data = cursor.fetchall()
    users = []
    for row in data:
        user = {'id': row[0], 'name': row[1], 'age': row[2]}
        users.append(user)
    conn.close()
    return jsonify(users)
