import math

# Raiz Quadrada Simples

def raiz_quadrada(num):
    raiz_quadrada = math.sqrt(num)

    return raiz_quadrada

print(raiz_quadrada(4))

# Arredondamento Inteligente
def arrendondamento(value):

    arredondar = math.floor(value), math.ceil(value), round(value)

    return arredondar

print("Valores arredondados", arrendondamento(70.54))
