
pessoas = []

while True:
    decisao = int(input('Digite 1 para adicionar uma pessoa ou 2 sara sair: '))
    if decisao == 2:
        break
    
    pessoa = {
        'nome': input('Digite seu nome: '),
        'Idade': input('Digite sua idade: '),
        'Altura': input('Digite sua altura: '),
        }

    pessoas.append(pessoa)
    
print(pessoas)
