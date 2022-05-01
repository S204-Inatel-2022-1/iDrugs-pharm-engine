Feature: Farmácia

    Serviço responsável pelo controle da parte da Farmácia.

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
        Given Cadastrando o tipo
            | ID | nome do tipo |
        When O funcionario edita o tipo do produto com id 1
            | Novo nome do tipo |
        Then Produto editado com sucesso!

    Scenario: Editar tipagem com erro ID não encontrado
        Given Cadastrando o tipo
            | ID | nome do tipo |
        When O funcionario edita o tipo do produto com id 47
            | Novo nome do tipo |
        Then Tipo não encontrado!

    Scenario: Editar tipagem com erro duplicidade
        Given Cadastrando o tipo
            | ID | nome do tipo |
        When O funcionario edita a tipagem do ID 1 com nome já cadastrado
            | Novo nome do tipo |
        Then Tipo já existe!

    Scenario: Excluir tipagem
        Given Cadastrando o tipo
            | ID | nome do tipo |
        When O funcionario exclui a tipagem do id 1
        Then Produto excluido com sucesso!

    Scenario: Excluir tipagem com erro ID não encontrado
        Given Cadastrando o tipo
            | ID | nome do tipo |
        When O funcionario exclui a tipagem do id 47
        Then Tipo não encontrado!

    Scenario: Listagem de todos os tipos
        When Funcionario lista todos os tipos cadastrados
        Then Listagem de tipos efetuado com sucesso!

    # Produto
    Scenario: Cadastrar produtos com sucesso
        When O funcionario cadastra um produto
            | nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
        Then Cadastrado com sucesso!

    Scenario: Cadastrar produto com erro de duplicidade
        Given Cadastrando produto
            | nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
        When O funcionario cadastra o produto que já possui o mesmo nome no registro
            | nome do produto duplicado | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
        Then Produto já existe! Erro!

    Scenario: Editar produto
        Given Cadastrando produto
            | ID | nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
        When O funcionario edita o produto com ID 1
            | Novo nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
        Then Produto Editado com sucesso!

    Scenario: Editar produto com erro ID não encontrado
        Given Cadastrando produto
            | ID | nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
        When O funcionario edita o produto com ID 47
            | Novo nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
        Then Produto não encontrado!

    Scenario: Editar produto com erro duplicidade
        Given Cadastrando produto
            | ID | nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
        When O funcionario edita o produto com ID 1 com nome já cadastrado
            | Novo nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
        Then Produto já existe!

    Scenario: Excluir produto
        Given Cadastrando produto
            | ID | nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
        When O funcionario exclui o produto com ID 1
        Then Produto Excluído com sucesso!

    Scenario: Excluir produto com erro ID não encontrado
        Given Cadastrando produto
            | ID | nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
        When O funcionario exclui o produto com ID 47
        Then Produto não encontrado!

    Scenario: Listagem de produtos de um tipo especifico
        Given Cadastrando o tipo
            | ID | nome do tipo |
        Given Cadastrando produto
            | ID | nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
        When Funcionario lista produtos do tipo "MEDICAMENTOS"
        Then Listado de produtos efetuado com sucesso!

    Scenario: Listagem de todos os produtos
        When Funcionario lista todos os produtos
        Then Listagem de produtos efetuado com sucesso!

    Scenario: Erro -> Listagem de produtos de um tipo especifico não cadastrado
        Given Cadastrando o tipo
            | ID | nome do tipo |
        Given Cadastrando produto
            | ID | nome do produto | marca | preço | tipo | Prescrição Médica | Classificação | Descrição | Foto | Bula |
        When Funcionario lista produtos do tipo "ARROZ"
        Then Erro ao listar produtos!


