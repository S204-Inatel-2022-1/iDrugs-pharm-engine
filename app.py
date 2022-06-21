import os

from flask import request, Blueprint, jsonify
from flask_cors import CORS

from config import app
from service.product import create_product, find_product, delete_product, find_product_id, find_product_type
from service.type import create_type, find_type, delete_type, find_type_id
from service.user import create_user, find_user, delete_user, find_user_id

blueprint = Blueprint('app', __name__, url_prefix='/idrugs-pharma-engine')

CORS(app)


# USER
@blueprint.route('/user', methods=['POST', 'PUT'])
def create_user_route():
    response = request.json
    return create_user(response)


@blueprint.route('/user', methods=['GET'])
def find_user_route():
    return find_user(request.json)

@blueprint.route('/user/<id>', methods=['GET'])
def find_user_id_route(id):
    return find_user_id(id)


@blueprint.route('/user', methods=['DELETE'])
def delete_user_route():
    response = request.json
    return delete_user(response)


# Tipo
@blueprint.route('/type', methods=['POST', 'PUT'])
def create_type_route():
    response = request.json
    return create_type(response)


@blueprint.route('/type', methods=['GET'])
def find_type_route():
    return find_type(request.json)

@blueprint.route('/type/<id>', methods=['GET'])
def find_type_id_route(id):
    return find_type_id(id)


@blueprint.route('/type', methods=['DELETE'])
def delete_type_route():
    response = request.json
    return delete_type(response)


# Produto
@blueprint.route('/product', methods=['POST', 'PUT'])
def create_product_route():
    response = request.json
    return create_product(response)


@blueprint.route('/product', methods=['GET'])
def find_product_route():
    return find_product(request.json)

@blueprint.route('/product/<id>', methods=['GET'])
def find_product_id_route(id):
    return find_product_id(id)

@blueprint.route('/product/type/<type>', methods=['GET'])
def find_product_type_route(type):
    return find_product_type(type)


@blueprint.route('/product', methods=['DELETE'])
def delete_product_route():
    response = request.json
    return delete_product(response)


@app.route('/')
def status():
    return jsonify({"message": "IDRUGS-PHARMA-ENGINE: Aplicação rodando"})


app.register_blueprint(blueprint)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8081))
    app.run(host='0.0.0.0', port=port)
