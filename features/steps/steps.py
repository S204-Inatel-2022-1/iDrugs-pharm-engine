import json

import requests as requests
from behave import when, then

urlTemplate = 'http://localhost:8080'

user = None

@when('Cadastrar o funcionario')
def cadastrar_o_funcionario(context):
    context.url = urlTemplate + '/user'
    context.headers = {'content-type': 'application/json'}
    context.body = {
        "name": "Ítalo",
        "email": "italo@gmail.com",
        "password": "abcdef123",
    }


@then('Cadastrado com sucesso!')
def cadastrado_com_sucesso(context):
    context.res = requests.post(context.url, data=json.dumps(context.body), headers=context.headers)
    assert context.res.status_code == 201
    assert json.loads(context.res.content)['name'] == context.body['name'] and json.loads(context.res.content)['email'] == context.body['email']

@then('Falha ao cadasrtar')
def falha_ao_cadasrtar(context):
    context.res = requests.post(context.url, data=json.dumps(context.body), headers=context.headers)
    assert json.loads(context.res.content)['message'] == 'Já existe um usuário cadastrado com esse email.'
    assert context.res.status_code == 400