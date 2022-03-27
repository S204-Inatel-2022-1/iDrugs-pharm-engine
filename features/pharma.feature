Feature: Farmácia

    Serviço responsável pelo controle da parte da Farmácia.

    Scenario: Cadastrar um usuário com sucesso
        When Cadastrar o funcionario
        Then Cadastrado com sucesso!

    Scenario: Cadastrar um usuário com erro
        When Cadastrar o funcionario
        Then Falha ao cadasrtar