
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

try:
    from .conf import DB_PATH
except ModuleNotFoundError as e:
    print("configure 'models/conf.py' from 'models/conf.py.sample'")
    exit(1)


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}'.format(DB_PATH)
db = SQLAlchemy(app)

