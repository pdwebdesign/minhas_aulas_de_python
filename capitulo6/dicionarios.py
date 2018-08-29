pedro = { "idade":28,"nome":"Pedro",}
maria = {"nome":"Maria", "idade":30}

pessoas = [pedro,maria]
for var in pessoas:
    if var["idade"] > 28:
        print(var["nome"])
        print(var["idade"])