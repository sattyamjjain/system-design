from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

app = Flask(__name__)
engine = create_engine(
    "mysql+pymysql://user:password@host/db_name?charset=utf8mb4",
    poolclass=QueuePool,
    pool_size=50,
    pool_recycle=3600,
    pool_timeout=10,
)
db = SQLAlchemy(app, engine_options={"pool_pre_ping": True})
