cadeia = input("Digite uma cadeia de caracteres:\n")
letra_a = "a"

for char in range(0,len(cadeia)):
    if cadeia[char] == "z":
        cadeia = cadeia.replace(cadeia[char], letra_a)
    else:
        print(cadeia[char])
        cadeia = cadeia.replace(cadeia[char], )

print(cadeia)

'''else:
        proximo = char + 1
        cadeia[char] = cadeia[proximo]'''
