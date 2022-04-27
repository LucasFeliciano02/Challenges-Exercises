
while True:
    nota = int(input('Digite a nota do aluno: '))
    if  0 <= nota <= 10:
        print(f'Nota armazenada com sucesso {nota}')
        break
    print('Nota inválida digite novamente')

# if nota >= 0 and nota <= 10: