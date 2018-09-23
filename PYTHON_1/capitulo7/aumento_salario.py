def calculaAumento(funcionario,aumento = 0.6):
    if funcionario["salario"]>1000:
        aumento = 0.20
    funcionario["salario"] *= 1 + aumento

funcionarios = {"nome":"Pedro Duarte","dataAdmissao":"2015-01-01","cargo":"supervisor","salario":1000}
print(funcionarios)
print(funcionarios["nome"] + " Salario antigo: " + str(funcionarios["salario"]))
calculaAumento(funcionarios,0.3)
print(funcionarios["nome"] + " Salario novo: " + str(funcionarios["salario"]))

