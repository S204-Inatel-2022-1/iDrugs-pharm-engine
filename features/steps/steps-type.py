import json
from json import loads

import requests as requests
from behave import when, then, given

urlTemplate = 'http://localhost:8080/type'

@given("Cadastrando tipagem {type}")
def step_impl(context, type):
    context.body = {
        "name": type
    }
    tipagem_cadastrado_com_sucesso(context)

@when("O funcionario cadastra o tipo do produto {type}")
def step_impl(context, type):
    context.body = {
        "name": type
    }


@then("Tipagem cadastrado com sucesso!")
def tipagem_cadastrado_com_sucesso(context):
    context.url = urlTemplate
    context.headers = {'content-type': 'application/json'}
    context.res = requests.post(context.url, data=json.dumps(context.body), headers=context.headers)
    assert context.res.status_code == 201
    assert json.loads(context.res.content)['name'] == context.body['name']
    print("----- CADASTRO -----")
    print(context.res.content)
    print("--------------------")


@then("Produto já existe! Erro!")
def step_impl(context):
    context.url = urlTemplate
    context.headers = {'content-type': 'application/json'}
    context.res = requests.post(context.url, data=json.dumps(context.body), headers=context.headers)
    assert context.res.status_code == 400
    print("----- ERRO DUPLICIDADE -----")
    print(context.res.content)
    print("--------------------")


@when('O funcionario edita o tipo {type}')
def step_impl(context, type):
    att = loads(context.text)
    id = search_type(type)
    context.body = {
        "_id": id['$oid'],
        "name": att['name']
    }

def search_type(type):
    response = requests.get(urlTemplate, params=type, headers={'content-type': 'application/json'})
    return json.loads(response.content)[0]['_id']


@then("Produto editado com sucesso!")
def step_impl(context):
    context.url = urlTemplate
    context.headers = {'content-type': 'application/json'}
    context.res = requests.put(context.url, data=json.dumps(context.body), headers=context.headers)
    assert context.res.status_code == 200
    assert json.loads(context.res.content)['name'] == context.body['name']
    print("----- EDIÇÃO -----")
    print(context.res.content)
    print("--------------------")

@when('O funcionario exclui {type}')
def step_impl(context, type):
    id = search_type(type)
    context.body = {
        "_id": id['$oid']
    }


@then("Tipo excluido com sucesso!")
def step_impl(context):
    context.url = urlTemplate
    context.headers = {'content-type': 'application/json'}
    context.res = requests.delete(context.url, data=json.dumps(context.body['_id']), headers=context.headers)
    assert json.loads(context.res.content)['message'] == 'Deletado com sucesso!'
    assert context.res.status_code == 200
    print("----- DELETADO -----")
    print(context.res.content)
    print("--------------------")

@then("Listagem efetuado com sucesso!")
def step_impl(context):
    context.url = urlTemplate
    context.headers = {'content-type': 'application/json'}
    context.res = requests.get(context.url, headers=context.headers)
    assert context.res.status_code == 200
    print("----- LISTAGEM -----")
    print(context.res.content)
    print("--------------------")