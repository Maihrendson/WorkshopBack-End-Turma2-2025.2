import math

# Raiz Quadrada Simples
def raiz_quadrada(num):
    raiz_quadrada = math.sqrt(num)

    return raiz_quadrada

print(raiz_quadrada(4))

# Arredondamento Inteligente
def arrendondamento(value):

    arredondar = ("Piso", math.floor(value)),("Teto", math.ceil(value)),("Arredondamento", round(value))

    return arredondar

print("Valores arredondados", arrendondamento(70.54))

#Calculadora Geométrica Avançada
class FiguraGeometrica():

    #Área do Circulo
    @staticmethod
    def area_circulo(raio):
        return math.pi * math.pow(raio, 2)
    print(area_circulo(7))

    #Área do triângulo
    @staticmethod
    def area_triangulo(base, altura):
        return (base * altura) / 2
    print(area_triangulo(2,6))

    #Hipotenusa
    @staticmethod
    def hipotenusa(cateto1, cateto2):
        return math.sqrt(math.pow(cateto1, 2) + math.pow(cateto2, 2))
    print(hipotenusa(3, 4))

