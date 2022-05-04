import json

from flask import request

from config import app
from service.type import create_type, find_type, delete_type
from service.user import create_user, find_user, delete_user


# USER
@app.route('/user', methods=['POST', 'PUT'])
def create_user_route():
    response = json.dumps(request.json)
    return create_user(response)

@app.route('/user', methods=['GET'])
def find_user_route():
    return find_user(request.args)

@app.route('/user', methods=['DELETE'])
def delete_user_route():
    response = json.dumps(request.json)
    return delete_user(response)

# Tipo
@app.route('/type', methods=['POST', 'PUT'])
def create_type_route():
    response = json.dumps(request.json)
    return create_type(response)

@app.route('/type', methods=['GET'])
def find_type_route():
    return find_type(request.args)

@app.route('/type', methods=['DELETE'])
def delete_type_route():
    response = json.dumps(request.json)
    return delete_type(response)



if __name__ == "__main__":
    app.run(port=8080, debug=True)