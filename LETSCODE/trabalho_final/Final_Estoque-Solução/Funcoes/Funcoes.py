'''
No programa guardamos uma lista de item
Cada item é uma lista com dois valores,
um representando o nome o outro o valor
Exemplo:
item = [Arroz,5.0]

listasItens =
[[Arroz,5.0],
 [Feijao,6.0],
 [Batata,3.0]]
'''

#A Função recebe o nome e o valor de um item.
#Adicione ele na lista de item, lembre-se quem um item uma lista com dois valores
def addItem(listaItens,nome,valor):
    item = [nome,valor]
    listaItens.append(item)

#A função recebe uma lista e um nome
#Encontre o item com o nome dado e remova da lista
def removerItem(listaItens,nome):
    for item in listaItens:
        nomeItem = item[0]
        if nomeItem == nome:
            listaItens.remove(item)




#A função recebe uma lista, um nome e um valor
#Encontre o itens cujo o nome contenha o nome dado ou tenha o mesmo valor
#Salve estes item em uma nova lista retorne esta lista
def filtro(listaItens,nome,valor):
    lista = []
    for item in listaItens:
        if nome == item[0]:
            lista.append(item)
    return lista

