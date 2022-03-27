import os

from dotenv import load_dotenv
from flask import Flask
from flask_pymongo import PyMongo

load_dotenv()

app = Flask(__name__)
app.env = os.getenv('ENV')

if app.env == 'DEV':
    app.config['MONGO_URI'] = os.getenv("MONGO_DEV")
elif app.env == 'TEST':
    app.config['MONGO_URI'] = os.getenv("MONGO_TEST")
elif app.env == 'PRD':
    app.config['MONGO_URI'] = os.getenv("MONGO_PRD")

mongo = PyMongo(app)