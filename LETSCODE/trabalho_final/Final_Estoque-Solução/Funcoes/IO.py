#Salve o lista de itens no arquivo com o nome dado
def salvandoArquivo(nomeArq,listaItens):
    arq = open(nomeArq,'w')
    for item in listaItens:
        nome = item[0]
        valor = item[1]
        arq.write("{},{}\n".format(nome,valor))
    arq.close()

#Crie uma lista com os itens salvos no arquivo com o nome dado
def lerArquivo(nomeArq):
    listaItem = []
    arq = open(nomeArq,'r')
    texto = arq.read()
    textoLinhas = texto.split('\n')[:-1]
    for linha in textoLinhas:
        item = linha.split(',')
        listaItem.append(item)
    arq.close()
    return listaItem

