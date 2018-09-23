class Pessoas(object):
    def __init__(self):
        self.nome = ""
        self.idade = 0
    def falar(self):
        print("oi")
    def morrer(self):
        self.nome = "ela morreu"


maria = Pessoas()
maria.nome = "Maria"
print(maria.nome)
maria.falar()
maria.morrer()
print(maria.nome)
