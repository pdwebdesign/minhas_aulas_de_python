import random
count = 0
soma = 0
numero = 10000000
while count <= numero:
    nota = random.randint(0, 10)
    soma = soma + nota
    media = soma / numero
    count = count + 1
print("SOMA: ",soma)
print("MEDIA: ", media)