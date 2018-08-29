numeroA = int(input("Digite o primeiro numero "))
numeroB = int(input("Digite o segundo numero "))
numeroC = int(input("Digite o terceiro numero\n"))

aux = 0
if (numeroA > numeroB):
    aux = numeroA
    numeroA = numeroB
    numeroB = aux

if (numeroB <= numeroC):
    print(numeroA,numeroB,numeroC)
else:
    if (numeroA<numeroC):
            print(numeroA,numeroC,numeroB)
    else:
        print(numeroC,numeroA,numeroB)
