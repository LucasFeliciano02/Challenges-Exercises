"""
Escreva um programa capaz de calcular o valor de um investimento por 10 anos futuro
"""

while True:
    try:
        inves_inicial = eval(input('Digite seu investimento: '))
        taxa_anual = eval(input('Digite a taxa anual: '))
        
        for i in range(10):
            inves_total = inves_inicial * (1 + taxa_anual)
        print(f'Com um investimento inicial de {inves_inicial}R$ com uma taxa de {taxa_anual}% ao ano, daqui a 10 anos o investidor terá um aumento para {inves_total}R$\n')
    
    except:
        print('Digite apenas numeros')