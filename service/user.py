import json

from bson import json_util
from flask import Response
from werkzeug.security import generate_password_hash

from config import mongo


def create_user(self):
    r = json.loads(self)
    name = r['name']
    passw = r['password']
    email = r['email']

    user = get_user_email(email)
    if user:
        response = json_util.dumps({'message': 'Já existe um usuário cadastrado com esse email.'})
        return Response(response, mimetype='application/json', status=400)

    hash_password = generate_password_hash(passw)
    id = mongo.db.user.insert_one(
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

def get_user_email(self):
    return mongo.db.user.find_one({'email': self})

