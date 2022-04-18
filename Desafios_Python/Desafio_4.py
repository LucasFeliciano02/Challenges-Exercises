"""
QUESTÃO: Defina uma classe que tenha pelo menos dois métodos: getString: para obter uma string do console input().
printString: para imprimir a string em maiúsculas. Também inclua uma função de teste simples para testar os métodos de classe.
"""

class EntrarString(object):
    def __init__(self, string):
        self.s = string
        
    def getString(self):
        self.s = input('Digite algo: ')
        
    def printString(self):
        print(self.s.upper())
        
        
strObg = EntrarString('')
strObg.getString()
strObg.printString()
