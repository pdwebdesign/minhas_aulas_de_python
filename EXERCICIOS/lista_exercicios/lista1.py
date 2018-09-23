#exercicio 12
'''altura = float(input("Digite sua altura"))
peso_ideal = (72.7*altura)-58
print("Seu peso ideial é: ",peso_ideal)'''


def uniao(a,b):
    for i in b:
        for ii in a:
            if b[i] == a[ii]:
                continue
            else:
                b.append(b[i])

# To test, uncomment all lines
# below except those beginning with >>>.

a = [1, 2, 3]
b = [2, 4, 6]
uniao(a,b)
print(a)
# >>> [1,2,3,4,6]
print(b)
# >>> [2,4,6]


