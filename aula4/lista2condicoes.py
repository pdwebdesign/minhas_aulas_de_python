letra = input("usuario, digite uma letra") #voce tinha colocado int
# mas isso é para tranformar
# em numero nao se usa qunado a gente quer texto mesmo.
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    #sua logica estava errada, quando você coloca !=, tem que ser and quando é igual
    #voce faz or, pense um pouco sobre isso.
    print("VOGAL")
else:
    print("CONSOANTE")