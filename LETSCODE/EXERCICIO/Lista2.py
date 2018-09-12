## PArte 1

# 1. Peça a idade do usuário e imprima se ele é maior ou menor de 18 ano.
idade = int(input("digite sua idade"))
if idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")

# 2. Peça um número e mostre se ele é positivo ou negativo;
num = int(input("digite um número"))
if num > 0:
    print("positivo")
elif num == 0:
    print("nulo")
else:
    print("negativo")

# 3. Dado um número digitado, mostre se ele é Par ou Ímpar
num2 = int(input("digite um número: "))
if num1 % 2 == 1:
    print("O numero é impar")
else:
    print("O numero é par")

# 4. Peça dois números e mostre o maior deles;
num1 = int(input("digite um número: "))
num2 = int(input("digite outro número: "))
if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)
else:
    print("iguais")


# 5. Faça um programa que leia a validade das informações:
#    a.Idade: entre 0 e 150;
idade = int(input("digite idade: "))
if 0 <= idade <= 150:
    print("OK")
else:
    print("erro")
#    b.Salario: maior que 0;
salario = float(input("digite seu salário: "))
if salario > 0:
    print("OK")
else:
    print("erro")
#    c.Sexo: M ou F;
sexo = input("digite seu sexo (F/M): ")
if sexo.upper() == 'F' or sexo.upper() == 'M':
    print("OK")
else:
    print("erro")

# 6. Escreve um programa que peça a nota de 3 provas de um aluno, e verifique se ele passou o não de ano:
m1 = float(input("nota 1: "))
m2 = float(input("nota 2: "))
m3 = float(input("nota 3: "))
media = (m1 + m2 + m3) / 4
if media > 6:
    print("aprovado")
else:
    print("Reprovado")


#7. Fazer um programa que mostre uma questão de múltipla escolha ..
enunciado = "Qual dessas é uma liguagem de computação famosa\n"\
            "a - Cobra\n"\
            "b - Ingles\n"\
            "c - Python\n"\
            "d - Runas\n"\
            "e - Nenhum das anteriores\n"
resposta = input(enunciado)
if enunciado == 'c':
    print("Acertou")
else:
    print("Errou")

#8 verificar quem é o assassino
pontos = 0
resposta1 = input("Telefonou para a vítima?")
if resposta1.lower() == "sim":
    pontos = pontos + 1 
resposta1 = input("Esteve no local do crime?")
if resposta1.lower() == "sim":
    pontos = pontos + 1 
resposta1 = input("Mora perto da vítima?")
if resposta1.lower() == "sim":
    pontos = pontos + 1 
resposta1 = input("Devia para a vítima?")
if resposta1.lower() == "sim":
    pontos = pontos + 1
resposta1 = input("Já trabalhou com a vítima?")
if resposta1.lower() == "sim":
    pontos = pontos + 1 

if pontos == 5:
    print("assassino")
elif pontos >= 3:
    print("cúmplices")
elif pontos == 2:
    print("suspeito")
if:
    print("Liberado")

#9 Verificar aumento do produto

##############
#  Desafio
##############
#1 - Faça um programa que leia 3 números e informe o maior deles

#modo 1
num1 = int(input("digite o 1º número: "))
num2 = int(input("digite o 2º  número: "))
num3 = int(input("digite o 3º  número: "))
if num1 > num2 and num1 > num3:
    print(num1, "é o maior")
elif num2 > num1 and num2 > num3:
    print(num2, "é o maior")
else:
    print(num3, "é o maior")

#Modo 2
num1 = int(input("digite o 1º número: "))
num2 = int(input("digite o 2º  número: "))
num3 = int(input("digite o 3º  número: "))
if num1 > num2:
    if num1 > num3:
        print(num1, "é o maior")
    else:
        print(num3, "é o maior")    
elif num2 > num1:
    if num2 > num3:
        print(num2, "é o maior")
    else:
        print(num3, "é o maior")


#2 - Agora faça com 4 números
num1 = int(input("digite o 1º número: "))
num2 = int(input("digite o 2º  número: "))
num3 = int(input("digite o 3º  número: "))
num4 = int(input("digite o 3º  número: "))
if num1 > num2 and num1 > num3 and num1 > num4:
    print(num1, "é o maior")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(num2, "é o maior")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(num3, "é o maior")
else:
    print(num4, "é o maior")

#3 - Diagnostico
A = input("Sente dor no corpo?")
B = input("Você tem febre?") 
C = input("Você tem tosse? ") 
D = input("Está com congestão nasal?") 
E = input("Tem manchas pelo corpo?")

A = A.lower() == 'sim'
B = B.lower() == 'sim'
C = C.lower() == 'sim'
D = D.lower() == 'sim'
E = E.lower() == 'sim'

if  A and B and (not C) and (not D) and E :
    print("Dengue")
elif  A and B and C and D and (not E) :
    print("Gripe")
elif  (not A) and B and C and D and (not E) :
    print("Gripe")
elif  A and (not B) and C and D and (not E) :
    print("Gripe")
else:
    print("Sem doenças")