from random import randint
perdeu = 0
ganhou = 0
trocou = 0
nao_trocou = 0


for i in range(0,100000):
    porta = randint(1,100)
    #print("porta:",porta)
    chute = randint(1,100)
    #print("chute:",chute)

    troca = randint(0,1)

    if troca == 1:
        trocou = trocou + 1
        if porta == chute:
            if troca == 1:
                perdeu = perdeu + 1
            else:
                ganhou = ganhou + 1
        else:
            if troca == 1:
                    ganhou = ganhou + 1
            else:
               perdeu = perdeu + 1

print("Trocou",trocou)
print("Ganhou:",ganhou)
print("Perdeu:",perdeu)

porcentagem = (ganhou/trocou)*100

print("porcentagem:",porcentagem)
