import os
import sys
from flask_sqlalchemy import SQLAlchemy

try:
    from .conf import DB_DIR, DB_NAME
except ModuleNotFoundError as e:
    print("configure 'models/conf.py' from 'models/conf.py.sample'")
    exit(1)

db_path = os.path.join(os.path.dirname(__file__) + '/../' + DB_DIR, DB_NAME)
track_modification = False
database_uri = 'sqlite:///{}'.format(db_path)

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    db.app = app
