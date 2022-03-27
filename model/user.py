
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def imprimi(self):
        print(f"Nome: {self.name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")