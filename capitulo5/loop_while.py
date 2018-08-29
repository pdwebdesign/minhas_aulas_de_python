import random

numero_a_adivinhar = random.randint(0,9)
acertei = False

while not acertei:
    numero = int(input("Adivinhe o numero que eu pensei, entre 0 e 9\n"))
    if numero == numero_a_adivinhar:
        print("parabens, voce adivinhou!")
        acertei = True
    else:
        print("tente novamente")