#Animais Simples

class Animal:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return 0
    
    def apresentar(self):
        return f"Olá eu sou {self.nome}, e tenho {self.idade}"
class Cachorro(Animal):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    def falar(self):
        return "Au Au!"

class Gato(Animal):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    def falar(self):
        return "Miau!"
    
gato = Gato("Felino", 19)
cachorro = Cachorro("Totó", 11)

animal = [gato, cachorro]

for Animal in animal:
    print(Animal.apresentar())
    print(Animal.falar())
    print()