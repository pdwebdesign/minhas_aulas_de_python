def raiz_quadrada(a,n):
    x = a
    contador = 1
    if n == 0:
        return a
    else:
        while contador < n:
            x_contador = (x + a/x)/2
            print(x_contador)
            x = x_contador
            contador = contador + 1
    return x_contador


x = float(input("Digite o valor de x:\n"))
n = int(input("Digite o valor de n:\n"))

print(raiz_quadrada(x,n))




