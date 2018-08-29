class Funcionario(object):
    def __init__(self, **kwargs):
        self.idade = kwargs.get("idade",0)
        self.nome = kwargs.get("nome", "")
        self.salario = kwargs.get("salario", "")
        self.sexo = kwargs.get("sexo", "")
    def aumento(self, fator=2):
        self.salario *= fator
        return self.salario
    def __str__(self):
        return "Nome: " + self.nome + ", idade: " + str(self.idade)

maria = Funcionario(nome="Maria da silva",salario = 1000,idade = 18)
print(maria)
