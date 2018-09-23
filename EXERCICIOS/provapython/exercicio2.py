'''Faça um programa que leia um número inteiro positivo e uma função
que informe se o número informado é ou não um ano bissexto.
Não utilizar módulos e funções prontas. Obs: um ano é bissexto se ele
for divisível por 400 ou se ele for divisível por 4 e não por 100.'''

def bissexto(numero):
    if numero % 400 == 0 or numero % 4 == 0 and not numero % 100 == 0:
        print("Esse ano é bissexto\n")
    else:
        print("Não é um ano bissexto")


numero = int(input("Digite um ano\n"))
bissexto(numero)