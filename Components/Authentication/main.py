from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    "alice": {"password": "password123", "email": "alice@example.com"},
    "bob": {"password": "password456", "email": "bob@example.com"},
}


@app.route("/authenticate", methods=["POST"])
def authenticate():
    username = request.json.get("username")
    password = request.json.get("password")
    if username in users and password == users[username]["password"]:
        return jsonify({"success": True, "email": users[username]["email"]})
    else:
        return (
            jsonify({"success": False, "message": "Invalid username or password"}),
            401,
        )


response = app.test_client().post(
    "/authenticate", json={"username": "alice", "password": "password123"}
)
print(response.get_json())
