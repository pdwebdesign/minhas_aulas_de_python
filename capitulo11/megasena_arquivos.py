arq = open('lista.txt', 'r')
file = open('vezes.txt','w')
texto = arq.readlines()

count = 0
lista = []
lista_new = []
maior = 0
menor = 1000000
for linha in texto:
    lista.append(linha)
    numero = lista[count].split()
    lista_new.append(numero)
    lista_new[count] = list(map(int, lista_new[count]))
    valor = sum(lista_new[count])
    if valor >= maior:
        maior = valor
    if valor < menor:
        menor = valor

    count += 1

print("A maior soma é :",maior)
print("A menor soma é :",menor)


print("TOTAL DE JOGOS:",count)

for j in range(1,61):
    numero = 0
    for i in range(0,count):
        numero+=lista_new[i].count(j)
    print("O numero",j,"aparece:",numero,"vezes")
    file.write("O numero %d" % j)
    file.write(" Apareceu: %d" % numero)
    file.write("\n")


#----------------------CODIGO PARA NUMEROS PARES E IMPARES---------------------
lista_texto =[]
for j in range(0,count):
    numero = 0
    numero_par = 0
    numero_impar = 0
    for i in range(0,6):
        numero = lista_new[j][i]
        if numero % 2 == 0:
            numero_par+=1
        else:
            numero_impar+=1
    par_texto = str(numero_par)
    impar_texto = str(numero_impar)
    lista_texto.append(par_texto+impar_texto)

print(count)
print("PAR - IMPAR | TOTAL |")
print(" 0  -   6     ",lista_texto.count("06"))
print(" 1  -   5     ",lista_texto.count("15"))
print(" 2  -   4     ",lista_texto.count("24"))
print(" 3  -   3     ",lista_texto.count("33"))
print(" 4  -   2     ",lista_texto.count("42"))
print(" 5  -   1     ",lista_texto.count("51"))
print(" 6  -   0     ",lista_texto.count("60"))



arq.close()
file.close()

