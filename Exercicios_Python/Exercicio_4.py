"""
Escreva um programa para obter raizes das equações quadraticas
"""

import math


while True:
    try:
        a = eval(input('Insira o coeficiente de A: '))
        b = eval(input('Insira o coeficiente de B: '))
        c = eval(input('Insira o coeficiente de C: '))    


        # Delta
        d = b*b - (4 * a * c)
        
        if d < 0:
            print('Delta < 0. Delta ∉ R')  # EX: a = 1, b = -4, c = 5
        elif d == 0:
            raiz = -b / (2*a)
            print(f'Delta = 0. Há uma única raiz real: {raiz}')  # EX: a = 4, b = -4, c = 1
        else:
            d = math.sqrt(d)  # square root
            raiz_1 = (-b + d) / (2 * a)    
            raiz_2 = (-b - d) / (2 * a)    
            print(f'Delta > 0. Há duas raízes reais, x e y respectivamente: {raiz_1, raiz_2}')  # EX: a = 1, b = -5, c = 6
    except:
        print('\nDigite apenas números\n')
        