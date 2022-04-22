
pessoas = []

while True:
    decisao = int(input('Digite 1 para cadastrar uma pessoa ou 2 para sair: '))
    if decisao == 2:
        break 
    
    pessoas.append(
            {'nome': input('Digite o nome: '),
             'idade': input('Digite a idade: '),
             'altura': input('Digite a altura: ')})
    
print(pessoas)
