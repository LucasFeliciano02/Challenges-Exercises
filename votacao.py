"""
pip install rich  =  Cor, animação
"""

import os
from rich import print


# 0s.linesep  =  Quebra de linha

# Constantes

VOTOS_X = 0
VOTOS_Y = 0

# Rodar eternamente
while True:
    # apresentar candidatos
    print('*'*20)
    print(f'[on green]TOTAL X:[/]{VOTOS_X}{os.linesep}[on red]TOTAL Y:[/]{VOTOS_Y}')
    print('*'*20)


# permita votar

    try:
        voto = int(input(f'Escolha seu voto{os.linesep}1 - X{os.linesep}2 - Y{os.linesep}seu voto: '))

        if voto == 1:
            VOTOS_X += 1
        elif voto == 2:
            VOTOS_Y += 1
        else:  # Considerando voto branco ou nulo
            pass 
    except:
        print('Digite apenas 1 ou 2')
    os.system('cls')  # Fica apenas em 1 linha 
