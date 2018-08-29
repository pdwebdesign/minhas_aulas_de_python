

def tabuada (numero):
    for i in range(1,11):
        total = numero * i
        print(numero , "X" , i , "=" , total)

numero = int(input("digite um numero"))
tabuada(numero)