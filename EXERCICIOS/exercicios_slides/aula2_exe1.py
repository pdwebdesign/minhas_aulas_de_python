#EXERCICIO 1 SLIDE 2
lista = [1,5,3,9,20,2,4]
menor = 10000000
maior = 0
for numero in lista:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print("maior: ",maior)
print("menor: ",menor)