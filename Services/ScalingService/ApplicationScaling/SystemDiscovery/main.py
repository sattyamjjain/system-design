from flask import Flask

# from flask_dyndns import DynDns

app = Flask(__name__)
# dd = DynDns(app)


@app.route("/")
def hello():
    return "Hello, world!"


if __name__ == "__main__":
    app.run()
