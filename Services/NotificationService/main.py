from flask import Flask, request
import redis

app = Flask(__name__)
redis_client = redis.Redis(host="localhost", port=6379)


@app.route("/notifications", methods=["POST"])
def send_notification():
    notification_data = request.get_json()
    channel = notification_data["channel"]
    message = notification_data["message"]
    redis_client.publish(channel, message)
    return "Notification sent"


def handle_notification(channel, message):
    print(f"Received message on channel {channel}: {message}")


if __name__ == "__main__":
    app.run(debug=True)
    pubsub = redis_client.pubsub()
    pubsub.subscribe("notifications")
    for message in pubsub.listen():
        handle_notification(message["channel"], message["data"])
