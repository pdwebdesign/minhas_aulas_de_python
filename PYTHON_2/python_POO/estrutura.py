class Conta :
    def __init__(self,numero ):
        self.numero = numero
        self.saldo = 0.0

conta = Conta(1)

print(conta.numero)
print(conta.saldo)