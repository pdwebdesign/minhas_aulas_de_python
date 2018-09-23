'''
Cria uma lista com 21 notas de 0 a 10, sem casas decimais. Em seguida, crie funções para mostrar a soma, média,
moda e mediana dos valores. Obs.: Moda é o número que mais aparece no conjunto de dados. Mediana é o valor que
divide o conjunto de dados ao meio.
'''
import random

def somar(lista):
    soma = 0
    for i in lista:
        soma = soma + i
    print("A soma da lista é", soma)
    return soma

def media(lista):
    soma = somar(lista)
    media = soma / len(lista)
    return media

def mediana(lista):
    numero = int(len(lista)/2)
    print("Mediana é :",lista[numero])

def moda(lista):
    maior = 0
    for i in range(0, len(lista)):
        if lista.count(lista[i]) > maior:
            maior = lista[i]
    print("O numero que mais aparece é o",maior)

lista = []
for i in range(0,21):
    numero = random.randint(0, 10)
    lista.append(numero)
print(lista)

somar(lista)
media(lista)
mediana(lista)
moda(lista)



