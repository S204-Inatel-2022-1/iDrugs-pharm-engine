import json

from flask import request

from config import app
from service.user import create_user, list_user, find_user, delete_user


# USER
@app.route('/user', methods=['POST', 'PUT'])
def create_user_route():
    response = json.dumps(request.json)
    return create_user(response)

@app.route('/user', methods=['GET'])
def list_user_route():
    return list_user()

@app.route('/user/search', methods=['GET'])
def find_user_route():
    return find_user(request.args)

@app.route('/user', methods=['DELETE'])
def delete_user_route():
    response = json.dumps(request.json)
    return delete_user(response)


if __name__ == "__main__":
    app.run(port=8080, debug=True)