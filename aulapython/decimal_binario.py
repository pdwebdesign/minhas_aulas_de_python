vet = [0]*8

while(True):
 binario = input("DIGITE O CODIGO BINARIO BYTE:")

 for i in range(8):
    vet[i] = int(binario[i])
 print(vet)

 soma = 0
 pot = 7
 for i in range(8):
    soma = soma + (vet[i] * (2 ** pot))
    pot = pot - 1
 print(soma)

