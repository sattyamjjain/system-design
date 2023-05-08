from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://user:password@host/db_name?charset=utf8mb4"
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_size": 20,
    "pool_recycle": 300,
    "pool_pre_ping": True,
    "pool_use_lifo": True,
    "pool_timeout": 30,
    "max_overflow": 10,
    "echo": True,
    "echo_pool": True,
    "pool_reset_on_return": "rollback",
}
db = SQLAlchemy(app)
