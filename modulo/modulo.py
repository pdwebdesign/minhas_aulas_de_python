#import bebida importa todas as bebidas
#from bebida import Cafe

#biblioteca math
#funcionalidades:
    #ceil
    #floor
    #trunc eliminar da virgula para a frente
    #pow potencia que é igual **
    #sqrt calcular raiz quadrada
    #factorial para calcular o fatorial de um numero

#se fizer import math vai fazer tudo
#se quiser so o sqrt a gente faz
#from math import sqrt (apenas calcular raiz quadrada)

#podemos importar duas fazendo:
#from math import sqrt, factorial

#EXEMPLO

import random

from math import sqrt


num2 = random.random()
print(num2)

num2 = random.randint(1,10)
print(num2)

num = int(input("DIGITE UM NUMERO:\n"))
raiz = sqrt(num) #quando fazemos com from math import sqrt nao precisa do math.sqrt
#print("A raiz de {} é igual a {} numero".format(num, math.ceil(raiz))) arredonda para cima
#print("A raiz de {} é igual a {} numero".format(num, math.ceil(raiz))) arredonda para baixo

print("A raiz de {} é igual a {} numero".format(num, raiz))

print("A raiz de {} é igual a {:.2f} numero".format(num, raiz))


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



