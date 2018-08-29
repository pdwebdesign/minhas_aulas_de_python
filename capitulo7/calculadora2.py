
def somar():
    numero1 = int(input("Digite o primeiro numero"))
    numero2 = int(input("Digite o segundo numero"))
    soma = numero1 + numero2
    print(soma)

while True:
    print("Digite 1 para somar\nDigite 2 para subtrair\nDigite 3 para sair")
    opcao = int(input("escolha um numero\n"))

    if opcao == 1:
        somar()

    if opcao == 3:
        break
