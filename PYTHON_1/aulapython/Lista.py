nomes = ["Amanda","Vinicius","Tiago","Pedro"]
salario = [1000,1200,1600,2000,850]
numeros = [5,8,15,2,0,3]
print(nomes)
nomes.insert(1,"Joao")
print(nomes)
nomes.append("ULTIMO")
print(nomes)
nomes.remove("Vinicius")
print(nomes)
del nomes[2]
print(nomes)
nomes.pop(0)
print(nomes)

for item in nomes:
        print(item)
        print(item+" 123")

print(salario)

for item in salario:
    if(item < 1500):
        item = item * 1.2
        print(item)

for indice, valor in enumerate(nomes):
    print("lista[%d] = %d" % (indice, valor))


