class Bola:
    def __init__(self):
        self.cor = ""
        self.circunferencia = 0
        self.material = ""

    def trocaCor(self, cor):
        self.cor = cor
    def mostraCor(self):
        print(self.cor)

# Teste da Classe
bola = Bola()
bola.trocaCor("Azul")
bola.mostraCor()
