import os

from dotenv import load_dotenv
from flask import Flask
from flask_pymongo import MongoClient

load_dotenv()

app = Flask(__name__)
app.env = os.getenv('ENV')

if app.env == 'DEV':
    mongo = MongoClient(os.getenv("MONGO_DEV"))
elif app.env == 'TEST':
    mongo = MongoClient(os.getenv("MONGO_TEST"))
elif app.env == 'PRD':
    mongo = MongoClient(os.getenv("MONGO_PRD"))

