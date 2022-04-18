"""
QUESTÃO: Escreva um programa que aceite uma sequÊncia de números separados por vírgulas do console e gere uma lista e uma tupla que contenha
todos os números. Suponha que a seguinte entrada seja fornecida ao programa: 12,37,63,31,15,87
Então a saída deve ser: ['12', '37', '63', '31', '15', '87'] ('12', '37', '63', '31', '15', '87')
"""

lista = '12', '37', '63', '31', '15', '87'
print(list(lista))

tupla = '12', '37', '63', '31', '15', '87'
print(tuple(tupla))


valores = input('Digite um numeros separados por , : ')

lista = valores.split(",")
tupla = tuple(lista)

print(lista)
print(tupla)