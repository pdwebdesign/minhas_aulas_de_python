file = open("arquivoteste.txt","wt")
file.write("Ola\n")
file.write("Tudo\n")
file.close()

file = open("arquivoteste.txt","r")
print(file.read())
file.close()