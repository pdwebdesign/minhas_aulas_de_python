
class Cliente(object):
    def __init__(self,nome,cpf,salario=0):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
    def compra(self):
        print("obrigado pela compra")

pedro = Cliente("Pedro","09995240629",1200)
print(pedro.salario)


