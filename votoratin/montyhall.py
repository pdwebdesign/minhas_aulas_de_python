from random import randint
contador_troca = 0
contador_nao_troca = 0

acertou = 0

acertou_trocando = 0
acertou_nao_trocando = 0


for i in range(0,100):
    porta = randint(1,3)
    print("porta:",porta)
    chute = randint(1,3)
    print("chute:",chute)
    troca = randint(0,1)
    print("troca:",troca)
    contador_troca = contador_troca + 1
    print("trocou")
    if chute == 1 and porta == 1:
        chute = randint(1,3)
        if chute == 1:
            acertou_nao_trocando = acertou_nao_trocando + 1
    if chute == 1 and porta == 2:
        chute = 3
    if chute == 1 and porta == 3:
        chute = 2
    if chute == 2 and porta == 2:
        chute = randint(1,3)
        if chute == 2:
            acertou_nao_trocando = acertou_nao_trocando + 1
    if chute == 2 and porta == 1:
        chute = 3
    if chute == 2 and porta == 3:
        chute = 1
    if chute == 3 and porta == 3:
        chute = randint(1,3)
        if chute == 3:
            acertou_nao_trocando = acertou_nao_trocando + 1
    if chute == 3 and porta == 1:
        chute = 2
    if chute == 3 and porta == 2:
        chute = 1


print("Trocou:",contador_troca," vezes.")
print("Nao trocou:",contador_nao_troca," vezes.")

print("Acertou trocando:",acertou_trocando," vezes.")
print("Acertou nao trocando:",acertou_nao_trocando," vezes.")

porcentagem_trocando = acertou_trocando / contador_troca
#porcentagem_nao_trocando = acertou_nao_trocando / contador_nao_troca

print("% acertou trocando:",porcentagem_trocando*100)
#print("% acertou nao trocando:",porcentagem_nao_trocando*100)


print("ACERTOU total: ", acertou)