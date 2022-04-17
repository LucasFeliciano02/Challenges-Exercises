"""
QUESTÃO: Escreva um programa que possa calcular o fatorial de um dado número. Os resultados devem ser impressos em uma
sequência separada por vírgulas em uma única linha. Suponha que a seguinte entrada
seja fornecida ao programa: 8 Então, a saída ser: 40320

"""

while True:
    try:
        def factorial(x):
            if x == 0:
                return 1
            return x * factorial(x - 1)

        x = int(input('Digite algum numero: '))
        print(factorial(x))
    except:
        print('\nDigite apenas números\n')
        