from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


@app.route("/timeline")
def get_timeline():
    user_id = request.args.get("user_id")
    start_time = request.args.get("start_time")
    end_time = request.args.get("end_time")
    conn = sqlite3.connect("timeline.db")
    cursor = conn.cursor()

    query = "SELECT * FROM events"
    if user_id:
        query += f" WHERE user_id = {user_id}"
    if start_time and end_time:
        query += f" AND timestamp BETWEEN {start_time} AND {end_time}"
    elif start_time:
        query += f" AND timestamp >= {start_time}"
    elif end_time:
        query += f" AND timestamp <= {end_time}"
    query += " ORDER BY timestamp ASC"
    cursor.execute(query)
    data = cursor.fetchall()
    events = []
    for row in data:
        event = {"id": row[0], "user_id": row[1], "timestamp": row[2], "data": row[3]}
        events.append(event)
    conn.close()
    return jsonify(events)


@app.route("/event", methods=["POST"])
def create_event():
    data = request.get_json()
    if "user_id" not in data or "timestamp" not in data or "data" not in data:
        return jsonify({"error": "Invalid data"}), 400
    conn = sqlite3.connect("timeline.db")
    cursor = conn.cursor()
    query = "INSERT INTO events (user_id, timestamp, data) VALUES (?, ?, ?)"
    cursor.execute(query, (data["user_id"], data["timestamp"], data["data"]))
    conn.commit()
    event_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": event_id}), 201
