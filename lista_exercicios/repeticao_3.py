cont = 0
while cont != 5:
    if cont == 0:
        nome = input("digite seu nome:\n")
        if len(nome) > 3:
            print("nome ok")
            cont = 1

    if cont == 1:
        idade = int(input("digite sua idade:\n"))
        if idade >= 0 and idade <= 150:
            print("idade ok")
            cont = 2

    if cont == 2:
        salario = float(input("digite seu salario:\n"))
        if salario > 0:
            print("salario ok")
            cont = 3

    if cont == 3:
        sexo = input("digite seu sexo:\n")
        if sexo == "f" or sexo == "m":
            print("sexo ok")
            cont = 4

    if cont == 4:
        estado_civil = input("digite seu estado civil:\n")
        if estado_civil == "s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d":
            print("estado civil ok")
            cont = 5
