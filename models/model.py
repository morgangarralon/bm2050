
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

try:
    from .conf import DB_PATH
except ModuleNotFoundError as e:
    print("configure 'models/conf.py' from 'models/conf.py.sample'")
    exit(1)


track_modification = False
database_uri = 'sqlite:////{}'.format(DB_PATH)

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)