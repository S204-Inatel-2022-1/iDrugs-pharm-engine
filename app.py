from flask import request, Blueprint

from config import app
from service.product import create_product, find_product, delete_product
from service.type import create_type, find_type, delete_type
from service.user import create_user, find_user, delete_user

blueprint = Blueprint('app', __name__, url_prefix='/idrugs-pharma-engine')

# USER
@blueprint.route('/user', methods=['POST', 'PUT'])
def create_user_route():
    response = request.data
    return create_user(response)

@blueprint.route('/user', methods=['GET'])
def find_user_route():
    return find_user(request.data)

@blueprint.route('/user', methods=['DELETE'])
def delete_user_route():
    response = request.data
    return delete_user(response)

# Tipo
@blueprint.route('/type', methods=['POST', 'PUT'])
def create_type_route():
    response = request.data
    return create_type(response)

@blueprint.route('/type', methods=['GET'])
def find_type_route():
    return find_type(request.data)

@blueprint.route('/type', methods=['DELETE'])
def delete_type_route():
    response = request.data
    return delete_type(response)

# Produto
@blueprint.route('/product', methods=['POST', 'PUT'])
def create_product_route():
    response = request.data
    return create_product(response)

@blueprint.route('/product', methods=['GET'])
def find_product_route():
    return find_product(request.data)

@blueprint.route('/product', methods=['DELETE'])
def delete_product_route():
    response = request.data
    return delete_product(response)

app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(port=8081, debug=True)