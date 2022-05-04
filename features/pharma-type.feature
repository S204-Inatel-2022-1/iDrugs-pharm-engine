@type
Feature: Tipagem

    Serviço responsável pelo controle da parte da Farmácia cadastro de tipos.

    # nome do produto = String
    # Marca = String
    # Preço = BigDecimal
    # Tipo = Enum -> Que o cliente cadastra
    # Prescrição Médica = Boolean (Precisa ou não de Prescrição Médica)
    # Classificação = Enum (Tarja pré cadastrada no sistema)
    # Descrição = String
    # Foto = String (Link da foto)
    # Bula = String (Link pdf da bula)

    # Tipo
    Scenario: Cadastrar tipagem
        When O funcionario cadastra o tipo do produto "medicamentos"
        Then Tipagem cadastrado com sucesso!

    Scenario: Cadastrar tipagem com erro de duplicidade
        Given Cadastrando tipagem "medicamentos"
        When O funcionario cadastra o tipo do produto "medicamentos"
        Then Produto já existe! Erro!

    Scenario: Editar tipagem
        Given Cadastrando tipagem "medicamentos"
        When O funcionario edita o tipo "medicamentos"
            """
                {
                    "name": "limpeza"
                }
            """
        Then Produto editado com sucesso!

    Scenario: Excluir tipagem
        Given Cadastrando tipagem "medicamentos"
        When O funcionario exclui "medicamentos"
        Then Tipo excluido com sucesso!

#    Scenario: Listagem de todos os tipos
#        Given Cadastrando tipagem "medicamentos"
#        Then Listagem efetuado com sucesso!

    # Produto
#    Scenario: Cadastrar produtos com sucesso
#        When O funcionario cadastra um produto
#            | nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
#        Then Cadastrado com sucesso!
#
#    Scenario: Cadastrar produto com erro de duplicidade
#        Given Cadastrando produto
#            | nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
#        When O funcionario cadastra o produto que já possui o mesmo nome no registro
#            | nome do produto duplicado | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
#        Then Produto já existe! Erro!
#
#    Scenario: Editar produto
#        Given Cadastrando produto
#            | ID | nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
#        When O funcionario edita o produto com ID 1
#            | Novo nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
#        Then Produto Editado com sucesso!
#
#    Scenario: Editar produto com erro ID não encontrado
#        Given Cadastrando produto
#            | ID | nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
#        When O funcionario edita o produto com ID 47
#            | Novo nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
#        Then Produto não encontrado!
#
#    Scenario: Editar produto com erro duplicidade
#        Given Cadastrando produto
#            | ID | nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
#        When O funcionario edita o produto com ID 1 com nome já cadastrado
#            | Novo nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
#        Then Produto já existe!
#
#    Scenario: Excluir produto
#        Given Cadastrando produto
#            | ID | nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
#        When O funcionario exclui o produto com ID 1
#        Then Produto Excluído com sucesso!
#
#    Scenario: Excluir produto com erro ID não encontrado
#        Given Cadastrando produto
#            | ID | nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
#        When O funcionario exclui o produto com ID 47
#        Then Produto não encontrado!
#
#    Scenario: Listagem de produtos de um tipo especifico
#        Given Cadastrando o tipo
#            | ID | nome do tipo |
#        Given Cadastrando produto
#            | ID | nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
#        When Funcionario lista produtos do tipo "MEDICAMENTOS"
#        Then Listado de produtos efetuado com sucesso!
#
#    Scenario: Listagem de todos os produtos
#        When Funcionario lista todos os produtos
#        Then Listagem de produtos efetuado com sucesso!
#
#    Scenario: Erro -> Listagem de produtos de um tipo especifico não cadastrado
#        Given Cadastrando o tipo
#            | ID | nome do tipo |
#        Given Cadastrando produto
#            | ID | nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
#        When Funcionario lista produtos do tipo "ARROZ"
#        Then Erro ao listar produtos!


