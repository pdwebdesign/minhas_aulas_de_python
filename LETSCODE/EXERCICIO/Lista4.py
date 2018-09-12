# #Exercicio 1
listaTexto = ["Arroz","Feijao","Batata"]
for item in listaTexto:
    print(item)

#Exercicio 2
num = int(input("Digite um numero:"))
for cont in range(len(num)):
    print(cont)

#Exercicio 4
num = int(input("Digite um numero:"))
quant = 0
for cont in range(num+1):
    if cont % 2 == 0:
        print(cont)
        quant += 1
print("quantidade",quant)

#Extra: como criar um lista aletoria
from random import randint

listaAle = []
for cont in range(10):
    valor = randint(0,10)
    listaAle.append(valor)

#exercicio 5
#1º Modo
maximo = 0
for item in listaAle:
    if item > maximo:
        maximo = item
print("maximo:",maximo)

#2º Modo
listaOrd = sorted(listaAle)
listaAle.sort()
print(listaAle)
print(listaAle[-1])
print(listaAle.pop())

#Exercicio 6
#1º Modo
for cont in range(3):
    maximo = max(listaAle)
    print(maximo)
    listaAle.remove(maximo)

#2º Modo
listaAle.sort()
listaReversa = list(reversed(listaAle))
print(listaReversa)
print(listaReversa[-3:])

#Exercicio 7
lista1 = [1,4,5]
lista2 = [2,2,3]
lista = []
for cont in range(len(lista1)):
    lista.append(lista1[cont] + lista2[cont])
print(lista)

#Exercicio 8
lista1 = [1,4,5]
lista2 = [2,2,3]
prod = 0
for cont in range(len(lista1)):
    prod += lista1[cont] + lista2[cont]
print(prod)

#Exercicio 9
lista = []
for cont in range(5):
    num = input("Digite um num:")
    lista.append(num)
print(lista)

#Exercicio 10
for cont in range(5):
    lista[0] = float(lista[0])
print(lista)

#Exercicio 11
soma = 0
for cont in range(4):
    nota = float(input('Digite uma nota:'))
    soma += nota
print("Media:",soma/4)

#-------------------------------------#
#          Desafios
#-------------------------------------#



