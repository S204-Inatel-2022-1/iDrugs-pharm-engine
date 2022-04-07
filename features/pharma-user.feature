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

    # Usuário
    Scenario: Cadastrar um usuário com sucesso
        When Cadastrar o funcionario
            """
                {
                    "name": "Ítalo",
                    "email": "itmoura@gmail.com",
                    "password": "minhasenha"
                }
            """
        Then Cadastrado com sucesso!

    Scenario: Cadastrar um usuário com erro
        Given Cadastrar o funcionario
            """
                {
                    "name": "Ítalo",
                    "email": "itmoura@gmail.com",
                    "password": "minhasenha"
                }
            """
        When Cadastrar o funcionario
            """
                {
                    "name": "Ítalo",
                    "email": "itmoura@gmail.com",
                    "password": "minhasenha"
                }
            """
        Then Falha ao cadastrar

    Scenario: Listagem de todos os funcionarios
        Given Cadastrar o funcionario
            """
                {
                    "name": "Ítalo",
                    "email": "itmoura@gmail.com",
                    "password": "minhasenha"
                }
            """
        Then Listagem dos funcionarios efetuado com sucesso!

    Scenario: Editar um usuário com sucesso
        Given Cadastrar o funcionario
            """
                {
                    "name": "Ítalo",
                    "email": "itmoura@gmail.com",
                    "password": "minhasenha"
                }
            """
        When Editar o funcionario com email "itmoura@gmail.com"
            """
                {
                    "name": "Ítalo Moura",
                    "email": "italo@gmail.com",
                    "password": "senha"
                }
            """
        Then Editado com sucesso!

    Scenario: Excluir um usuário com sucesso
        Given Cadastrar o funcionario
            """
                {
                    "name": "Ítalo",
                    "email": "itmoura@gmail.com",
                    "password": "minhasenha"
                }
            """
        When Excluir o funcionario com email "itmoura@gmail.com"
        Then Exclusão efetuada com sucesso!