import json
import re

from bson import json_util, ObjectId
from flask import Response

from config import mongo, bd_table

db = mongo.get_database(bd_table).product

def create_product(self):
    r = json.loads(self)
    id = r.get('_id')
    name = r.get('name')
    brand = r.get('brand')
    price = r.get('price')
    type = r.get('type')
    prescription = r.get('prescription')
    description = r.get('description')
    photo = r.get('photo')
    leaflet = r.get('leaflet')
    if id is not None:
        return edit_product(id, name, brand, price, type, prescription, description, photo, leaflet)

    product = get_product_name(name, type)
    if product:
        response = json_util.dumps({'message': 'Produto já cadastrado'})
        return Response(response, mimetype='application/json', status=400)

    id = db.insert_one(
        {'name': name, 'brand': brand, 'price': price, 'type': type, 'prescription': prescription, 'description': description, 'photo': photo, 'leaflet': leaflet}
    )
    jsonDate = {
        'id': str(id.inserted_id),
        'name': name,
        'brand': brand,
        'price': price,
        'type': type,
        'prescription': prescription,
        'description': description,
        'photo': photo,
        'leaflet': leaflet
    }
    response = json_util.dumps(jsonDate)
    return Response(response, mimetype='application/json', status=201)

def edit_product(id, name, brand, price, type, prescription, description, photo, leaflet):
    db.update_one(
        {'_id': ObjectId(id)},
        {'$set': {'name': name, 'brand': brand, 'price': price, 'type': type, 'prescription': prescription, 'description': description, 'photo': photo, 'leaflet': leaflet}}
    )
    jsonDate = {
        'id': str(id),
        'name': name,
        'brand': brand,
        'price': price,
        'type': type,
        'prescription': prescription,
        'description': description,
        'photo': photo,
        'leaflet': leaflet
    }
    response = json_util.dumps(jsonDate)
    return Response(response, mimetype='application/json', status=200)

def get_product_name(name, type):
    return db.find_one({'name': name, 'type': type})

def list_product():
    find = db.find({})
    if find:
        response = json_util.dumps(find)
        return Response(response, mimetype='application/json', status=200)
    response = json_util.dumps({'message': 'Nenhum registro encontrado'})
    return Response(response, mimetype='application/json', status=400)

def find_product(self):
    if self is not None:
        args = json.loads(self)
        name = args.get('name')
        brand = args.get('brand')
        leaflet = args.get('leaflet')
        filter = {}
        if name is not None:
            rgx = re.compile('.*'+name+'.*', re.IGNORECASE)
            filter['name'] = rgx
        if brand is not None:
            rgx = re.compile('.*'+brand+'.*', re.IGNORECASE)
            filter['brand'] = rgx
        if leaflet is not None:
            rgx = re.compile('.*'+leaflet+'.*', re.IGNORECASE)
            filter['leaflet'] = rgx
        response = json_util.dumps(db.find(filter))
        return Response(response, mimetype='application/json', status=200)
    else:
        return list_product()

def find_product_id(id):
    if id is not None:
        response = json_util.dumps(db.find_one({'_id': ObjectId(id)}))
        return Response(response, mimetype='application/json', status=200)

def find_product_type(type):
    if type is not None:
        response = json_util.dumps(db.find({'type': type}))
        return Response(response, mimetype='application/json', status=200)



def delete_product(self):
    r = json.loads(self)
    id = r.get('_id')
    find = db.delete_one({'_id': ObjectId(id)})
    if find:
        response = json_util.dumps({'message': 'Deletado com sucesso!'})
        return Response(response, mimetype='application/json', status=200)
    response = json_util.dumps({'message': 'Id não encontrado'})
    return Response(response, mimetype='application/json', status=400)
