
print("Olá, mundo!")
      
""" O terminal acusou um erro de syntaxe na linha 1
e falou que se faz necessário fechar os parênteses "()"
para que o erro seja solucionado """

nome = "Maihrendson"

print(nome)

""" O terminal acusou um erro de variável
acusando que não existe uma variável para "nome" """

def somar(a, b):
    return a + b

resultado = somar(10, 5)
print(resultado)

""" O terminal acusou que não é suportado usar uma soma de uma variável do tipo inteiro 
com uma variável do tipo String """

numeros = [10, 20, 30]

try:
    indice = int(input("Digite um índice para acessar a lista: "))


    print(numeros[indice])
        

except IndexError:

    print("Valor inválido")

except ValueError:

    print("Valor inválido, tente novamente!!")



""" O terminal acusou um erro que indica que a o indice da lista
ele está fora do intervalo da lista """

def dividir(a, b):
    return a / b

try:

    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")


    resultado = dividir(int(num1), int(num2))

    print(f"Resultado: {resultado}")

except ValueError:

    print ("Não é possível realizar a divisão, Use números inteiros")

except ZeroDivisionError:

    print ("Não é possível realizar divisão com 0")


""" O terminal ele está retornando um numero de tipo float
porém estamos fazendo o cálculo como inteiro
se por algum acaso entrarmos com um float no input o código quebra """

dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

try:

    chave = input("Digite a chave que deseja acessar: ").lower()

    print(f"O valor da chave '{chave}' é: {dados[chave]}")

except KeyError:

    print("Essa chave não existe, coloque uma chave válida Por Favor!!")

""" O terminal acusou uma key inexistente
para outro tipo de chave que não existe nos dados"""