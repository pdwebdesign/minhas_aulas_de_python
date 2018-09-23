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