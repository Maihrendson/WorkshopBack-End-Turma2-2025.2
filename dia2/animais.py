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
    #Bloco que faz a herança da classe Animal
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    def falar(self):
        return "Au Au!"

class Gato(Animal):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    def falar(self):
        return "Miau!"
class Zoologico:
    
    def __init__(self):
        self.animais = []
    #Adicona animais ao zoologico
    def adicionar_animal(self, animal):
        self.animais.append(animal)
        return f"Animal adicionado com sucesso: {animal.nome}"
    #Lista os animais
    def listar_animais(self):
        for a in self.animais:
            print(f"{a.nome} | {a.idade} | {a.falar()}")
    #Filtra animais por um tipo especifico 
    def filtrar_por_tipo(self, tipo):
        filtrados = [a for a in self.animais if isinstance(a, tipo)]
        return filtrados

#Cria uma variavel zoo para a Classe Zologico e adiciona animais
zoo = Zoologico()
zoo.adicionar_animal(Cachorro("Rex", 5))
zoo.adicionar_animal(Gato("Mimi", 3))
zoo.adicionar_animal(Cachorro("Totó", 7))
zoo.adicionar_animal(Gato("Peluto", 1))

#Lista os animais existentes no zoologico
print("\nAnimais no zoológico:")
zoo.listar_animais()

#Filtra animais por gato e cachorro
print("\nFiltrando só gatos:")
for b in zoo.filtrar_por_tipo(Gato):
    print(b.nome)

print("\nFiltrando só cachorros:")
for b in zoo.filtrar_por_tipo(Cachorro):
    print(b.nome)