import json
from json import loads

import requests as requests
from behave import when, then, given

urlTemplate = 'http://localhost:8080'

user = None

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
    context.url = urlTemplate + '/type'
    context.headers = {'content-type': 'application/json'}
    context.res = requests.post(context.url, data=json.dumps(context.body), headers=context.headers)
    assert context.res.status_code == 201
    assert json.loads(context.res.content)['name'] == context.body['name']
    print("----- CADASTRO -----")
    print(context.res.content)
    print("--------------------")


@then("Produto já existe! Erro!")
def step_impl(context):
    context.url = urlTemplate + '/type'
    context.headers = {'content-type': 'application/json'}
    context.res = requests.post(context.url, data=json.dumps(context.body), headers=context.headers)
    assert context.res.status_code == 400
    print("----- ERRO DUPLICIDADE -----")
    print(context.res.content)
    print("--------------------")