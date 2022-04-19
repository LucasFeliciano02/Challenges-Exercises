"""
Escreva um programa para converter a temperatura Celsius em Fahrenheit
"""

while True:
    try:
        celsius = float(input('Digite uma temperatura em Celsius: '))

        fahenheit = (9/5)*celsius + 32

        print(f'\n{celsius}°C convertido para Fahenheit é: {fahenheit}°F\n')

        if fahenheit < 30:
            print('Está muito frio\n')
        elif fahenheit > 31 and fahenheit < 89:
            print('Temperatura normal\n')
        else:
            print('Está muito quente\n')
    except:
        print('Digite apenas numeros')
