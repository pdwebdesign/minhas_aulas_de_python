'''
#EXERCICIO 1 SLIDE 1
nota1 = int(input("digite a primeira nota\n"))
nota2 = int(input("digite a primeira nota\n"))
nota3 = int(input("digite a primeira nota\n"))
nota4 = int(input("digite a primeira nota\n"))

media = (nota1+nota2+nota3+nota4)/4
print(nota1,nota2,nota3,nota4,media)


#EXECICIO 2 SLIDE 1
meses = ["janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
print(meses)
escolha = int(input("Digite um numero de 1 a 12"))
print(meses[escolha-1])

#EXERCICIO 3 SLIDE 1
vetor1 = [1,6,3,4,2]
vetor2 = [2,7,8,5,3]

vetor3 = [vetor1[0],vetor1[2],vetor1[1],vetor1[4],vetor1[3]]

#EXERCICIO 4 SLIDE 1
while True:
    a = int(input("digite numero 1"))
    b = int(input("digite numero 2"))
    c = int(input("digite numero 3"))

    if a > b:
        if b > c:
            print(a,b,c)
        elif a > c:
            print(a,c,b)
        else:
            print(c,a,b)
    elif a > c:
        print(b,a,c)
    elif b > c:
        print(b,c,a)
    else:
        print(c,b,a)


#EXERCICIO 5 SLIDE 1

a = int(input("digite a\n"))
b = int(input("digite b\n"))
c = int(input("digite c\n"))

delta = (b**2) - (4*a*c)

if delta < 0:
    print("delta negativo")
else:
    raiz_1 = (-b + (delta)**(1/2))/(2*a)
    print("Raiz 1: ",raiz_1)
    raiz_2 = (-b - (delta)**(1/2))/(2*a)
    print("Raiz 2: ",raiz_2)

'''

#EXERCICIO 1 SLIDE 2

A = [-1,5,10,-3,8,15,4,-10,9,0]

if len(A) <= 1:
    print(A)
else:
    for j in range(0,len(A)):
        for i in range(0,len(A)-1):
            if A[i]>A[i+1]:
                Aux = A[i+1]
                A[i+1] = A[i]
                A[i] = Aux
    print(A)





