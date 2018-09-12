## Exercicio 1
num = int(input("Digite um numero:"))
cont = 1
while cont <= num:
    print(cont)
    cont += 1 #cont = cont+1

# #Exercicio 2
num = int(input("Digite um numero:"))
cont = 0
resultado = 0
while cont < num:
    cont += 1
    resultado += cont
print("Somatorio é",resultado)

#Exercicio 3
num = int(input("Digite um numero:"))
cont = 0
resultado = 1
while cont < num:
    cont += 1 #cont = cont + 1
    print(cont,end='*')
    resultado *= cont #resultado = resultado * cont
print(":",resultado)

#Exercicio 4 : Simples
while cont <= 10:
    resultado = num * cont
    # print(cont,"*",num,":",resultado)
    print("{} * {} = {}".format(cont, num, resultado))
    cont += 1

#Exercicio 4: Tabuada completa
num = 0
while num < 10:
    num += 1
    cont = 1
    while cont <= 10:
        resultado = num * cont
        #print(cont,"*",num,":",resultado)
        print("{} * {} = {}".format(cont,num,resultado))
        cont += 1
    print("-----------------")

#Exercicio 5
num = int(input("Digite  um numero"))
cont = 1
while cont < num:
    if num%cont == 0:
        print(cont)
    cont +=1

#Exercicio 6
num = int(input("Digite um numero (Digite 0 para sair):"))
while num != 0:
    num = int(input("Digite um numero (Digite 0 para sair):"))

#Exercicio 7
idade = int(input("Digite a idade:"))
salario = float(input("Digite o salario:"))
sexo = input("Digite o sexo (M|F):")
while (idade > 0 or idade < 150) and (salario > 0) and (sexo == 'M' or sexo == 'F'):
    idade = int(input("Digite a idade:"))
    salario = float(input("Digite o salario:"))
    sexo = input("Digite o sexo (M|F):")
print("Entrada invalida")

#-------------------------------------#
#          Desafios
#-------------------------------------#
#Desafio 1

#Desafio 2

#Desafio Aula1
from random import  randint
min = 0
max = 10
segredo = randint(min,max)
num = round((min + max)/ 2)
tentativas = 1
while num != segredo:
    tentativas += 1
    print(num)
    if num < segredo:
        min = num
    else:
        max = num
    num = round((min + max)/ 2)
print("Acertou, num tentativas:",tentativas)

