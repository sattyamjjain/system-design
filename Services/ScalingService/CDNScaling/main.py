from flask import Flask
from flask_cdn import CDN

app = Flask(__name__)
app.config["CDN_DOMAIN"] = "yourcdn.com"
app.config["CDN_HTTPS"] = True
app.config["CDN_S3_BUCKET"] = "yourbucketname"
app.config["CDN_QUERYSTRING_REVISION"] = True
cdn = CDN(app)


@app.route("/")
def hello():
    return "Hello, world!"


if __name__ == "__main__":
    app.run()
