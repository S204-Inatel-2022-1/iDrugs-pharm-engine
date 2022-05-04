from config import mongo, bd_table

def before_scenario(context, feature):
    mongo.get_database(bd_table).drop_collection(feature.effective_tags[0])