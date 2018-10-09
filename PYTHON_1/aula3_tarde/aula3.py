count = 0
soma = 0
while count <= 3:
    nota = int(input("Digite uma nota:\n"))
    soma = soma + nota
    count = count + 1
print("SOMA: ",soma)
media = soma / 4
print("MEDIA: ", media)
