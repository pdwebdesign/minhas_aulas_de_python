hora  = input("informe a hora do dia, entre 0 e 23:\n")
hora = int(hora)
if hora >= 0 and hora <= 23:
    if hora >= 0 and hora < 12:
            print("bom dia!!\n")

    if hora >= 12 and hora < 18:
            print("boa tarde\n")

    if hora >= 18:
        print("Boa noite")
else:
    print("invalida")
'''
    idade = input("informe sua idade\n")
    idade = int(idade)
    if idade > 18:
        print("voce ja pode dirigir automovel")
    else: 
        print("voce ainda nao pode dirigir automovel")    
'''

'''
    hora = input(""informe a hora do dia, entre 0 e 23:\n")
    hora = int(hora)
    
    if hora >= 0 and hora < 12:
        print("Bom dia")
    elif hora >= 12 and hora < 18:
        print("Boa tarde")
    else:
        print("Boa noite")        
'''

