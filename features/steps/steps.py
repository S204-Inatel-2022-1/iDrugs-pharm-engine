import json
from json import loads

import requests as requests
from behave import when, then, given

urlTemplate = 'http://localhost:8080'

user = None

@given("Cadastrar o funcionario")
def step_impl(context):
    att = loads(context.text)
    context.url = urlTemplate + '/user'
    context.headers = {'content-type': 'application/json'}
    context.body = {
        "name": att['name'],
        "email": att['email'],
        "password": att['password'],
    }
    context.res = requests.post(context.url, data=json.dumps(context.body), headers=context.headers)

@when('Cadastrar o funcionario')
def cadastrar_o_funcionario(context):
    att = loads(context.text)
    context.body = {
        "name": att['name'],
        "email": att['email'],
        "password": att['password'],
    }

@then('Cadastrado com sucesso!')
def cadastrado_com_sucesso(context):
    context.url = urlTemplate + '/user'
    context.headers = {'content-type': 'application/json'}
    context.res = requests.post(context.url, data=json.dumps(context.body), headers=context.headers)
    assert context.res.status_code == 201
    assert json.loads(context.res.content)['name'] == context.body['name'] and json.loads(context.res.content)['email'] == context.body['email']
    print("----- CADASTRO -----")
    print(context.res.content)
    print("--------------------")

@then('Falha ao cadastrar')
def falha_ao_cadasrtar(context):
    context.url = urlTemplate + '/user'
    context.headers = {'content-type': 'application/json'}
    context.res = requests.post(context.url, data=json.dumps(context.body), headers=context.headers)
    assert json.loads(context.res.content)['message'] == 'Já existe um usuário cadastrado com esse email.'
    assert context.res.status_code == 400

@then("Listagem dos funcionarios efetuado com sucesso!")
def step_impl(context):
    context.url = urlTemplate + '/user'
    context.headers = {'content-type': 'application/json'}
    context.res = requests.get(context.url, headers=context.headers)
    assert context.res.status_code == 200
    print("----- LISTAGEM -----")
    print(context.res.content)
    print("--------------------")


@when('Editar o funcionario com email {email}')
def step_impl(context, email):
    att = loads(context.text)
    id = search_email(email)
    context.body = {
        "_id": id['$oid'],
        "name": att['name'],
        "email": att['email'],
        "password": att['password'],
    }

def search_email(email):
    response = requests.get(urlTemplate + '/user/search', params=email, headers={'content-type': 'application/json'})
    id = json.loads(response.content)[0]['_id']
    return id


@then("Editado com sucesso!")
def step_impl(context):
    context.url = urlTemplate + '/user'
    context.headers = {'content-type': 'application/json'}
    context.res = requests.put(context.url, data=json.dumps(context.body), headers=context.headers)
    assert context.res.status_code == 200
    assert json.loads(context.res.content)['name'] == context.body['name'] and json.loads(context.res.content)['email'] == context.body['email']
    print("----- EDIÇÃO -----")
    print(context.res.content)
    print("--------------------")


@when('Excluir o funcionario com email {email}')
def step_impl(context, email):
    id = search_email(email)
    context.body = {
        "_id": id['$oid']
    }


@then("Exclusão efetuada com sucesso!")
def step_impl(context):
    context.url = urlTemplate + '/user'
    context.headers = {'content-type': 'application/json'}
    context.res = requests.delete(context.url, data=json.dumps(context.body['_id']), headers=context.headers)
    assert json.loads(context.res.content)['message'] == 'Deletado com sucesso!'
    assert context.res.status_code == 200
    print("----- DELETADO -----")
    print(context.res.content)
    print("--------------------")