class Macaco(object):
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def verBucho(self):
        print('Bucho:', self.bucho)

    def digerir(self):
        if (len(self.bucho) > 0):
            self.bucho.pop()
