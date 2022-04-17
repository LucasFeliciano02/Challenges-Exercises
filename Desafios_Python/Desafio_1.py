"""
QUESTÃO: Escreva um programa que encontre todos os números DIVISÍVEIS POR 7, mas que não sejao MÚLTIPLOS DE 5, entre 2000 e 3200
(ambos incluídos). Os números obtidos devem ser impressos em sequência separada por vírgulas em uma única linha.
"""

lista_multiplos= []

for n in range(2000, 3201):
    if (n % 7 == 0) and (n % 5 != 0):
        lista_multiplos.append(str(n))

print(','.join(lista_multiplos))
