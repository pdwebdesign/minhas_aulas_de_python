import random
from math import *

computador1 = random.randint(0,100)
cont = 0
inicio = 0
fim = 100
print("NUMERO QUE TEM QUE ACERTAR:", computador1)
pivo = (inicio + fim)/2
pivo = floor(pivo)
while computador1 != pivo:
    cont = cont + 1
    print("CONT:",cont)
    pivo = (inicio + fim)/2
    pivo = floor(pivo)
    print("NUMERO QUE TENTEI:",pivo)
    if pivo < computador1:
        inicio = pivo
    if pivo > computador1:
        fim = pivo