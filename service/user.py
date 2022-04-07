import json
import re

from bson import json_util, ObjectId
from flask import Response
from werkzeug.security import generate_password_hash

from config import mongo

db = mongo.db.user

def create_user(self):
    r = json.loads(self)
    id = r.get('_id')
    name = r.get('name')
    passw = r.get('password')
    email = r.get('email')
    if id is not None:
        return edit_user(id, name, passw, email)

    user = get_user_email(email)
    if user:
        response = json_util.dumps({'message': 'Já existe um usuário cadastrado com esse email.'})
        return Response(response, mimetype='application/json', status=400)

    hash_password = generate_password_hash(passw)
    id = db.insert_one(
        {'name': name, 'email': email, 'password': hash_password}
    )
    jsonDate = {
        'id': str(id.inserted_id),
        'name': name,
        'password': hash_password,
        'email': email
    }
    response = json_util.dumps(jsonDate)
    return Response(response, mimetype='application/json', status=201)

def edit_user(id, name, passw, email):
    if passw is not None:
        hash_password = generate_password_hash(passw)
        db.update_one(
            {'_id': ObjectId(id)},
            {'$set': {'name': name, 'email': email, 'password': hash_password}}
        )
        jsonDate = {
            'id': str(id),
            'name': name,
            'email': email
        }
        response = json_util.dumps(jsonDate)
        return Response(response, mimetype='application/json', status=200)
    db.update_one(
        {'_id': ObjectId(id)},
        {'$set': {'name': name, 'email': email}}
    )
    jsonDate = {
        'id': str(id),
        'name': name,
        'email': email
    }
    response = json_util.dumps(jsonDate)
    return Response(response, mimetype='application/json', status=200)

def get_user_email(email):
    return db.find_one({'email': email})

def list_user():
    find = db.find({}, {'password':0})
    if find:
        response = json_util.dumps(find)
        return Response(response, mimetype='application/json', status=200)
    response = json_util.dumps({'message': 'Nenhum registro encontrado'})
    return Response(response, mimetype='application/json', status=400)

def find_user(args):
    if args:
        name = args.get('name')
        email = args.get('email')
        filter = {}
        if email is not None:
            filter['email'] = email
        if name is not None:
            rgx = re.compile('.*'+name+'.*', re.IGNORECASE)
            filter['name'] = rgx

        response = json_util.dumps(db.find(filter))
        return Response(response, mimetype='application/json', status=200)


def delete_user(id):
    r = json.loads(id)
    find = db.delete_one({'_id': ObjectId(r)})
    if find:
        response = json_util.dumps({'message': 'Deletado com sucesso!'})
        return Response(response, status=200)
    response = json_util.dumps({'message': 'Id não encontrado'})
    return Response(response, status=400)
