import random
from math import *
from datetime import datetime
jogadas = 10000
soma = 0
t0 = datetime.now()
for i in range(0,jogadas):
    cont = 0
    inicio = 0
    fim = 100000
    computador1 = random.randint(10, 90000)
    pivo = (inicio + fim)/2
    pivo = floor(pivo)
    pivo = pivo + 1
    while computador1 != pivo:
        cont = cont + 1
        #print("CONT:",cont)
        pivo = (inicio + fim)/2)
        pivo = floor(pivo)
        #print("NUMERO QUE TENTEI:",pivo)
        if pivo < computador1:
            inicio = pivo +1
        if pivo > computador1:
            fim = pivo -1
    soma = soma + cont
t1 = datetime.now()
media = soma/jogadas
print("A media de tentativas é :",media)
print("TEMPO GASTO:",t1-t0)