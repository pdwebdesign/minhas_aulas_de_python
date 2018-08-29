class Despesas(object):
    def __init__(self,**dicionario):
        self.nome = dicionario.get("nome","")#funcao get para pegar a chave nome e criar ela como vazia
        self.valor = dicionario.get("valor",0)

    def setdespesa(self,valor):
        if valor > 0:
            print("despesa ta positiva, é um erro")
        else:
            self.valor = valor

    def imprimir(self):
        print(self.nome)
        print(self.valor)
        print("\n")

class Entretenimento(Despesas):
    def __init__(self,**dicionario):
        super(Entretenimento,self).__init__(**dicionario)
    def imprimir(self):
        print(self.nome)
    def __str__(self):
       return "Nome :" + self.nome

entretenimento = Entretenimento(nome = "Cinema", valor = 10)
entretenimento.setdespesa(-100000)
entretenimento.imprimir()
despesinha = Despesas(nome = "Despesinha",valor = 10)
despesinha.imprimir()


print(entretenimento)
