class Funcionario(object):
    def __init__(self,**dicionario):
        self.nome = dicionario.get("nome","")
        self.idade = dicionario.get("idade",0)
        self.sexo = dicionario.get("sexo","")
        self.salario = dicionario.get("salario","")
    def __str__(self):
        return str(self.salario)
    def __add__(self, other):
        return self.salario + other

class Gerente(Funcionario):
    def __init__(self,**dicionario):
        super(Gerente, self).__init__(**dicionario)
        self.fator_aumento = 0.5



maria = Funcionario(nome="Maria Silva",idade=23,sexo="F",salario=2000)
#maria.imprimir()
pedro = Gerente(nome="Pedro",idade=28,sexo="M",salario=3000)
#pedro.imprimir()
print(maria + 0)
print(maria + 2000)
print(maria)