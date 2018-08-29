#FAÇA UM PROGRAMA QUE VERIFICA A
# IDADE E DIZ SE PODE DIRIGIR


idade = 1

while(idade != -1):
    idade = input("qual sua idade?\n")
    idade = int(idade)

    if idade >=18:
            print("voce pode dirigir")
    elif idade > 14:
        print("voce e adolescente")
    elif idade > 0:
        print("e uma criança")
print("exit")
