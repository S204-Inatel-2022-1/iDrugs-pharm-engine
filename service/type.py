import json
import re

from bson import json_util, ObjectId
from flask import Response

from config import mongo

db = mongo.db.type

def create_type(self):
    r = json.loads(self)
    id = r.get('_id')
    name = r.get('name')
    if id is not None:
        return edit_user(id, name)

    type = get_type_name(name)
    if type:
        response = json_util.dumps({'message': 'Tipo já cadastrado'})
        return Response(response, mimetype='application/json', status=400)

    id = db.insert_one(
        {'name': name}
    )
    jsonDate = {
        'id': str(id.inserted_id),
        'name': name
    }
    response = json_util.dumps(jsonDate)
    return Response(response, mimetype='application/json', status=201)

def edit_user(id, name):
    db.update_one(
        {'_id': ObjectId(id)},
        {'$set': {'name': name}}
    )
    jsonDate = {
        'id': str(id),
        'name': name
    }
    response = json_util.dumps(jsonDate)
    return Response(response, mimetype='application/json', status=200)

def get_type_name(name):
    return db.find_one({'name': name})

def list_type():
    find = db.find({})
    if find:
        response = json_util.dumps(find)
        return Response(response, mimetype='application/json', status=200)
    response = json_util.dumps({'message': 'Nenhum registro encontrado'})
    return Response(response, mimetype='application/json', status=400)

def find_type(args):
    if args:
        name = args.get('name')
        filter = {}
        if name is not None:
            rgx = re.compile('.*'+name+'.*', re.IGNORECASE)
            filter['name'] = rgx
        response = json_util.dumps(db.find(filter))
        return Response(response, mimetype='application/json', status=200)
    else:
        list_type()


def delete_type(id):
    r = json.loads(id)
    find = db.delete_one({'_id': ObjectId(r)})
    if find:
        response = json_util.dumps({'message': 'Deletado com sucesso!'})
        return Response(response, status=200)
    response = json_util.dumps({'message': 'Id não encontrado'})
    return Response(response, status=400)
