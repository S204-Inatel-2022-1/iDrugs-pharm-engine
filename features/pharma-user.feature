@user
Feature: Farmácia

    Serviço responsável pelo controle da parte da Farmácia.

    # nome = String
    # sobrenome = String
    # cargo = String
    # email = String
    # senha = String
    # link foto = String

    # Usuário
    Scenario: Cadastrar um usuário com sucesso
        When Cadastrar o funcionario
            """
                {
                    "name": "Ítalo",
                    "last_name": "Moura",
                    "photo_link": "fotolink.jpg",
                    "office": "Gerente",
                    "last_name": "Moura",
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
                    "last_name": "Moura",
                    "photo_link": "fotolink.jpg",
                    "office": "Gerente",
                    "email": "itmoura@gmail.com",
                    "password": "minhasenha"
                }
            """
        When Cadastrar o funcionario
            """
                {
                    "name": "Ítalo",
                    "last_name": "Moura",
                    "photo_link": "fotolink.jpg",
                    "office": "Gerente",
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
                    "last_name": "Moura",
                    "photo_link": "fotolink.jpg",
                    "office": "Gerente",
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
                    "last_name": "Moura",
                    "photo_link": "fotolink.jpg",
                    "office": "Gerente",
                    "email": "itmoura@gmail.com",
                    "password": "minhasenha"
                }
            """
        When Editar o funcionario com email "itmoura@gmail.com"
            """
                {
                    "name": "Ítalo",
                    "last_name": "Moura",
                    "photo_link": "fotolink.jpg",
                    "office": "Gerente",
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
                    "last_name": "Teste",
                    "photo_link": "fotolink.jpg",
                    "office": "Gerente",
                    "email": "itmoura@gmail.com",
                    "password": "minhasenha"
                }
            """
        When Excluir o funcionario com email "itmoura@gmail.com"
        Then Exclusão efetuada com sucesso!