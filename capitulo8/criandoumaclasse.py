'''funcionario = {"nome": "Maria","idade":23,
               "altura":1.65,"salario":1000}


funcionario["nome"] = "Maria"
funcionario["idade"] = 23
funcionario["salario"] = 1000
'''

class Funcionario(object):
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.salario = 0
    def aumento(self,aumento = 2):
        self.salario *= aumento

maria = Funcionario()
print(maria.nome)
print(maria.idade)
print(maria.salario)


maria.nome = "Maria da Silva"
maria.idade = 23
maria.salario = 1000

print(maria.nome)
print(maria.idade)
print(maria.salario)

#maria.aumento(3)


#print(maria.nome)
#print(maria.idade)
#print(maria.salario)


