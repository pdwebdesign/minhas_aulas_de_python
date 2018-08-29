import random

numero_a_adivinhar = random.randint(0,100)
acertei = False

while not acertei:
    numero = int(input("Adivinhe o numero que eu pensei, entre 0 e 9\n"))
    if numero == numero_a_adivinhar:
        print("parabens, voce adivinhou!")
        acertei = True
    else:
        if numero < numero_a_adivinhar:
            print("Meu numero e maior que o seu! Tente novamente\n")
        if numero > numero_a_adivinhar:
            print("meu numero e menor que o seu! Tente novamente \n")
        if numero_a_adivinhar % 2 == 0:
            print("O numero a adivinhar é par!\n")
        else:
            print("O numero a adivinhar e impar!\n")
        acertei = False