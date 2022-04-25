# if, else, elif

while True:
    try: 
        aluno = input('Digite o nome do aluno: ')

        nota1 = float(input('Digite sua 1º nota: '))
        nota2 = float(input('Digite sua 2º nota: '))
        nota3 = float(input('Digite sua 3º nota: '))
        nota4 = float(input('Digite sua 4º nota: '))

        media = (nota1 + nota2 + nota3 + nota4) / 4

        print(f'A media final foi de {media:.0f} pontos')

        if media >= 60:
            print(f'aluno {aluno} foi APROVADO')
        elif media >= 40:
            print(f'aluno {aluno} foi para RECUPERAÇÃO')
        else:
            print(f'aluno {aluno} foi REPROVADO')
    except:
        print('Escreva apenas numeros')
        