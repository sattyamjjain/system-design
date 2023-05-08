from flask import Flask
from gunicorn.app.base import BaseApplication

app = Flask(__name__)


@app.route("/", methods=["GET"])
def handle_request():
    return "Hello, World!"


class GunicornApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        for key, value in self.options.items():
            self.cfg.set(key, value)

    def load(self):
        return self.application


# Run the gunicorn server to scale the application
if __name__ == "__main__":
    options = {"bind": "0.0.0.0:8000", "workers": 4, "worker_class": "sync"}
    GunicornApplication(app, options).run()
