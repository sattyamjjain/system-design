from flask import Flask, request, jsonify

app = Flask(__name__)


class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email


users = []


@app.route('/users', methods=['POST'])
def add_user():
    user_data = request.get_json()
    user = User(len(users) + 1, user_data['name'], user_data['email'])
    users.append(user)
    return jsonify({'success': True})


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.get_json()
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        return jsonify({'success': False, 'message': 'User not found'})
    user.name = user_data.get('name', user.name)
    user.email = user_data.get('email', user.email)
    return jsonify({'success': True})


if __name__ == '__main__':
    app.run(debug=True)
