while True:
    numero_inteiro = input('digite um numero inteiro: ')

    if numero_inteiro.isdigit():  # isdigit = Checa se a string pode ser convertida em numero inteiro
        numero_inteiro = int(numero_inteiro)

        if numero_inteiro % 2 == 0:  # quando % MODULO DE NUMERO INTEIR0 FOR IGUAL 0  ou seja: de 2 em 2 = par
            print(f'{numero_inteiro} é par')
        else:
            print(f'{numero_inteiro} é impar')  # se nao for de 2 em 2 é impar
    else:
        print('isso nao é um numero inteiro')  # n com virgula
