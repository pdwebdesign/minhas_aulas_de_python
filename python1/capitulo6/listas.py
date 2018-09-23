anos = [1,2,6,10,4,20]
print(anos)
anos.sort()
print(anos)


'''
for j in range(0,len(anos)):
    for i in range(0,len(anos)-1):
        if anos[i] > anos[i+1]:
            aux = anos[i+1]
            anos[i+1] = anos[i]
            anos[i] = aux
print(anos)'''





'''
print(anos)
#buscando  elemento pelo o indice
print(anos[0])
print(anos[3])

#Também podemos saber qual é o tamanho da
# lista e quantos elementos ela tem.
#Isso é feito através do comando ”len”:

anos = [1970, 2010, 2012, 2017]
print(len(anos))

#manipulacao de elementos dentro da lista

#insert(pos,elem)
#adiciona uma novo elemento elem, na posicao pos

anos = [1970, 2010, 2012, 2017]
print(anos)
anos.insert(3, 2015)
print(anos)


#append(elem)
#adiciona um novo elemento elem no fim da lista

anos.append(2020)
print(anos)

#remove(elem)
#remove o elemento elem, que existe na lista

anos.remove(2010)
print(anos)

#pop()
#remove o ultimo elemento da lista, retornando

anos.pop()
print(anos)

anos.sort()
print(anos)

print(sorted(anos))
print(anos)

anos.remove(anos[0])

print(anos)
'''