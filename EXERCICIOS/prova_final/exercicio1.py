ips = ["192.168.0.34","255.255.255.0","10.255.255.255","192.168.255.255","172.31.255.255"]
nomes = ["www.google.com.br","www.faceboo.com","www.brasil.com","japao","teste"]

def procura(valor):
    while valor != "exit":
        valor = input("digite uma string\n")
        if len(valor) == 0:
            print("voce nao digitou nada")
        else:
            for i in range(0,len(ips)):
                if valor == ips[i]:
                    print("achou o ip:")
                    print("posicao : ",i)
                    print("nome = ",nomes[i])
                    break
            for j in range(0,len(nomes)):
                if valor == nomes[j]:
                    print("achou o nome:")
                    print("posicao : ",j)
                    print("ip = ",ips[j])
                    break

valor = ""
procura(valor)
