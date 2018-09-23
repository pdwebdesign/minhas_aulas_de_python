nomes = ["Amanda","Vinicius","Tiago","Pedro"]
Menu = "1 - Digitar seu nome\n" \
           "2 - Deletar nome\n" \
           "3 - Imprimir lista de nome\n" \
           "0 - Sair"

def Func():
    opcao = -1
    while (opcao != 0):
        print(Menu)
        opcao = input("Digite a opção:")
        opcao = int(opcao)
        if opcao == 1:
            nomeNovo = input("Digite o nome:")
            nomes.append(nomeNovo)
        elif opcao == 2:
            nomeDelete = input("Digite o nome para deletar:")
            if nomeDelete in nomes:
                nomes.remove(nomeDelete)
        elif opcao == 3:
            print(nomes)
        elif opcao == 4:
            nomes.sort()
            print(nomes)
        elif opcao == 0:
            print("Obrigado por ser nosso cliente")
        else:
            print("opção invalida")


Func()