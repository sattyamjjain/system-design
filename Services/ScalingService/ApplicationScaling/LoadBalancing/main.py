from flask import Flask

# from flask_loadbalancer import LoadBalancer

app = Flask(__name__)
app.config["LOADBALANCER_BACKENDS"] = [
    "http://localhost:5000",
    "http://localhost:5001",
    "http://localhost:5002",
]
# lb = LoadBalancer(app)


@app.route("/")
def hello():
    return "Hello, world!"


if __name__ == "__main__":
    app.run()
