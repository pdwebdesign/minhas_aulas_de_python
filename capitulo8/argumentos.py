class Funcionario(object):
    def __init__(self,**recebe):
        self.nome = recebe.get("nome","")
        self.idade = recebe.get("idade",0)
        self.salario = recebe.get("salario",0)
    def aumento(self,aumento = 2):
        self.salario *= aumento
    def editar_idade(self,idade):
        self.idade = idade
    def aumentar_idade(self):
        self.idade += 1


maria = Funcionario(nome="Maria",salario=1000,idade=23)
print(maria.nome)
print(maria.idade)
print(maria.salario)
maria.editar_idade(30)
print(maria.idade)
maria.aumentar_idade()
print(maria.idade)
maria.aumentar_idade()
print(maria.idade)
