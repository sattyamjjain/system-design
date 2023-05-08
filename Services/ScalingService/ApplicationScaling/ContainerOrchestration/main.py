from flask import Flask

# from flask_kubernetes import Kubernetes

app = Flask(__name__)
# k8s = Kubernetes(app)


@app.route("/")
def hello():
    return "Hello, world!"


if __name__ == "__main__":
    app.run()
