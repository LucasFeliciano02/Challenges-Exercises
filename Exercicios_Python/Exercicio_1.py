"""
Escreva um programa para calcular a média de 2 notas de exame:
"""

from sympy import Lambda


nota_1 = float(input('Digite sua nota 1: '))
nota_2 = float(input('Digite sua nota 2: '))

media = (nota_1 + nota_2)/2
print(f'A média é de: {media}')


print('\nMédia com função\n')

 
def media2(nota_1, nota_2):
    return (float(nota_1) + float(nota_2)) /2

nota_1 = input('Digite sua nota 1: ')
nota_2 = input('Digite sua nota 2: ')

print(f'A média é de: {media2(nota_1, nota_2)}')
