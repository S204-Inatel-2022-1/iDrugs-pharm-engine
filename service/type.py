import json
import re

from bson import json_util, ObjectId
from flask import Response

from config import mongo, bd_table

db = mongo.get_database(bd_table).type

def create_type(self):
    r = json.loads(self)
    id = r.get('_id')
    name = r.get('name')
    if id is not None:
        return edit_type(id, name)

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

def edit_type(id, name):
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

def find_type(self):
    if self is not None:
        args = json.loads(self)
        name = args.get('name')
        filter = {}
        if name is not None:
            rgx = re.compile('.*'+name+'.*', re.IGNORECASE)
            filter['name'] = rgx
        response = json_util.dumps(db.find(filter))
        return Response(response, mimetype='application/json', status=200)
    else:
        return list_type()

def find_type_id(id):
    if id is not None:
        response = json_util.dumps(db.find_one({'_id': ObjectId(id)}))
        return Response(response, mimetype='application/json', status=200)


def delete_type(self):
    r = json.loads(self)
    id = r.get('_id')
    find = db.delete_one({'_id': ObjectId(id)})
    if find:
        response = json_util.dumps({'message': 'Deletado com sucesso!'})
        return Response(response, status=200)
    response = json_util.dumps({'message': 'Id não encontrado'})
    return Response(response, status=400)
