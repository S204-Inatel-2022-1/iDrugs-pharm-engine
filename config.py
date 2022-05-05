import os

from dotenv import load_dotenv
from flask import Flask
from flask_pymongo import MongoClient

load_dotenv()

app = Flask(__name__)
app.env = os.getenv('ENV')

mongo = MongoClient('mongodb+srv://admin:Z4AfmmErlf7ftV98@cluster0.ayyzp.mongodb.net/')

bd_table = app.env