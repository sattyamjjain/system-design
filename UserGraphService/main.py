from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    friends = db.relationship(
        'User',
        secondary='friendships',
        primaryjoin='User.id==friendships.c.user_id',
        secondaryjoin='User.id==friendships.c.friend_id',
        backref=db.backref('friend_of', lazy='dynamic')
    )


friendships = db.Table(
    'friendships',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('friend_id', db.Integer, db.ForeignKey('user.id'))
)


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.name for user in users])


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'})
    return jsonify({'name': user.name, 'friends': [friend.name for friend in user.friends]})


@app.route('/users', methods=['POST'])
def create_user():
    name = request.json.get('name')
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id})


@app.route('/users/<int:user_id>/friends', methods=['POST'])
def add_friend(user_id):
    friend_id = request.json.get('friend_id')
    user = User.query.get(user_id)
    friend = User.query.get(friend_id)
    if user is None or friend is None:
        return jsonify({'error': 'User or friend not found'})
    if friend in user.friends:
        return jsonify({'error': 'Already friends'})
    user.friends.append(friend)
    db.session.commit()
    return jsonify({'message': 'Friend added'})


if __name__ == '__main__':
    db.create_all()
    app.run()
