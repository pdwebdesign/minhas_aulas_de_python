'''funcionario = {"Nome" : "Joao", "Salario" : 800, "Altura" : 1.72}
print(funcionario)
print(funcionario["Nome"])
funcionario["Profissao"] = "Professor"
print(funcionario)

Login = {"Login" : "admin", "Senha" : "admin"}
entrada = input("DIGITE LOGIN:")
if entrada == Login["Login"]:
    senha = input("Digite sua senha")
    if senha == Login["Senha"]:
            print("OK")
    else:
            print("Senha errada")
else:
       print("LOGIN ERRADO")'''

Dicionario = {"if" : "se" , "else" : "se nao" ,"while" : "enquanto", "for" : "Pecorrer lista"}
for item in Dicionario:
        print("%s : %s" % (item, Dicionario[item]))