n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite um numero inteiro: '))
n3 = int(input('Digite um numero inteiro: '))


if n1 > n2 and n1 > n3:
    print(f'O maior número é: {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior número é: {n2}')  
elif n3 > n2 and n3 > n1:
    print(f'O maior número é: {n3}')  
