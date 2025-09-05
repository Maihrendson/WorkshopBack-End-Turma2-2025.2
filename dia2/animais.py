#Animais Simples

class Animal:

    def falar(self):
        return "Emitir som"
    
class Cachorro(Animal):
    def falar(self):
        return "Au Au!"
    
class Gato(Animal):
    def falar(self):
        return "Miau!"
    
print(Cachorro().falar())
print(Gato().falar())