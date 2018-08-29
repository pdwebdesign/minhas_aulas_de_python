class Macaco:
    def __init__(self,nome):
        self.nome = nome
        self.bucho = []
    def ver_bucho(self):
        for i in range(0,len(self.bucho)):
            print(self.bucho[i])
    def comer(self,alimento):
        self.bucho.append(alimento)
    def digerir(self,alimento):
        self.bucho.remove(alimento)

macaco1 = Macaco("Paulo")
macaco2 = Macaco("Pedro")

macaco1.ver_bucho()
macaco2.ver_bucho()
macaco1.comer("alface")
macaco2.comer("carne")
macaco1.comer("banana")
macaco2.comer("morango")
macaco1.ver_bucho()
macaco2.ver_bucho()
#macaco1.digerir("alface")
#macaco2.digerir("carne")
macaco1.ver_bucho()
macaco2.ver_bucho()
macaco1.comer(macaco2.bucho)
macaco1.ver_bucho()
macaco2.comer(macaco1.bucho)
macaco2.ver_bucho()