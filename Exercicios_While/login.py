
usuario_bd = 'Lucas'
senha_bd = '123'


while True:
    usuario = input('Digite o usuario: ')
    senha = input('Digite a senha: ')

    if usuario == usuario_bd and senha == senha_bd:
        print('Entrou')
        break
    print('Deu ruim')
    