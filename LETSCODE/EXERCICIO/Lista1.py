## PARTE 1

# 1. Faça um Programa que mostre a mensagem "Alô mundo" na tela.
print("Alô mundo")

# 2. Faça um Programa que peça um número e mostre a mensagem "O número informado foi [número]".
n = input("digite um número: ")
print("O número informado foi", n)

# 3. Faça um Programa que peça dois números e imprima a soma.
n1 = int(input("digite um número: "))
n2 = int(input("digite outro número: "))
print('a soma é:', n1 + n2)

# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
m1 = float(input("nota 1: "))
m2 = float(input("nota 2: "))
m3 = float(input("nota 3: "))
m4 = float(input("nota 4: "))
print("média:", (m1 + m2 + m3 + m4) / 4)

# 5. Faça um Programa que converta metros para centímetros.
n = float(input("digite um número em metros: "))
print("o número digitado em centímetros é:", n * 100)

# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. Obs: Formula da área de um círculo, A = 3.14*r²
r = float(input("digite o raio de um círculo: "))
print("a área desse círculo é", 3.14 * r * r)

# 7.Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
l = float(input("digite o lado de um quadrado: "))
print("o dobro da área desse quadrado é", 2 * l * l)

# 8.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
salario = float(input("digite o quanto você ganha por hora: "))
horas = float(input("digite a quantidade de horas que você trabalha por mês: "))
print("você recebe", horas * salario, "por mês")

# 9.Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).
F = float(input("digite a temperatura em Farenheit: "))
print("a temperatura digitada, em Celsius, é:", 5 * (F - 32) / 9)

# 10.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
C = float(input("digite a temperatura em Celsius: "))
print("a temperatura digitada, em Farenheit, é:", C * 9 / 5 + 32)

# 11.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
i1 = int(input('digite um número inteiro: '))
i2 = int(input('digite outro número inteiro: '))
r1 = float(input('agora digite um número real: '))
# a. o produto do dobro do primeiro com metade do segundo.
print("o produto do dobro do primeiro com metade do segundo:", 2 * i1 * i2 / 2)
# b. a soma do triplo do primeiro com o terceiro.
print("a soma do triplo do primeiro com o terceiro:", 3 * i1 + r1)
# c. o terceiro elevado ao cubo.
print("o terceiro elevado ao cubo:", r1 ** 3)

# 12.Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) –58
altura = float(input('digite sua altura:'))
print("seu peso ideal é", 72.7 * altura - 58)

# 13.Faça um programa que peça o peso e altura e calcule o IMC da pessoa.
altura = float(input('digite sua altura em m:'))
peso = float(input('digite seu peso em kg:'))
print("seu imc é", peso / (altura ** 2))
