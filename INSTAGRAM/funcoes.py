def imprime(palavra,texto):
    if palavra in texto:
        return len(palavra)
    else:
        return -1

numero = imprime("Du","Pedro Pedro Duarte")
print(numero)

