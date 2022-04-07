from config import mongo

db = mongo.db.user

def before_scenario(context, feature):
    db.delete_many({})