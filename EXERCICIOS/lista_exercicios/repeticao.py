#exericio 1

acertou = False
while not acertou:
    numero = int(input("Digite um numero entre 0 e 10"))
    if numero > 0 and numero < 10:
        break
        print("OK NUMERO TA CERTO\n")
    else:
        print("O NUMERO NAO ESTA ENTRE 0 e 10\n")
        acertou = False
'''
def bubbleSort(A):
    if len(A) <= 1:
        sA = A
    else:
        for j in range(0,len(A)):
            for i in range(0,len(A)-1):
                if A[i]>A[i+1]:
                    Aux = A[i+1]
                    A[i+1] = A[i]
                    A[i] = Aux
        sA = A

    return sA

lista = [1,7,9,8,4]
bubbleSort(lista)
print(lista)

nota1 = int(input("digite a primeira nota\n"))
nota2 = int(input("digite a primeira nota\n"))
nota3 = int(input("digite a primeira nota\n"))
nota4 = int(input("digite a primeira nota\n"))

media = (nota1+nota2+nota3+nota4)/4
print(nota1,nota2,nota3,nota4,media)

#Crie uma lista de strings com todos os meses do ano e solicite
# solicite a entrada um numero numero 1 a 12 .
# Imprima o nome do mês de acordo com o número digitado.

#EXERCICIO 7 DA LISTA DE ESTRUTURA DE REPETICAO
#Faça um programa que leia 5 numeros e informe o maior numlero.


maior = 0
for num in range(1,5):
    numero = int(input("Digite o primeiro numero:"))
    if numero > maior:
        maior = numero

print(maior)


#EXERCICIO 8 DA LISTA DE ESTRUTURA DE REPETICAO
#Faça um programa que leia 5 numeros e informe a soma e média dos numeros.

numero = int(input("Digite o primeiro numero:"))
numero1 = int(input("Digite o primeiro numero:"))
numero2 = int(input("Digite o primeiro numero:"))
numero3 = int(input("Digite o primeiro numero:"))
numero4 = int(input("Digite o primeiro numero:"))
soma = 0
lista = [numero,numero1,numero2,numero3,numero4]
for num in lista:
    soma = soma + num
media = soma/5

print("Soma\n",soma)
print("Media",media)


#exercicio 9
#Faca um programa que imrpima na tela apenas os numeros impare entre 1 e 50
for j in range(1,50):
    if j % 2 != 0:
        print(j)


numero = 2.6
numero = int(numero)
print(numero)

'''

