
class User:
    def __init__(self, name, email, password, photo_link, office, last_name):
        self.name = name
        self.last_name = last_name
        self.office = office
        self.email = email
        self.password = password
        self.photo_link = photo_link

    def imprimi(self):
        print(f"Nome: {self.name}")
        print(f"Sobrenome: {self.last_name}")
        print(f"Cargo: {self.office}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print(f"Link Foto: {self.photo_link}")