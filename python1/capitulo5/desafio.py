import random
from datetime import datetime

jogadas=0
soma=0
tentativas = 10000
t0 = datetime.now()

while jogadas < tentativas:
    inicio = 0
    fim = 900000
    cont = 0

    jogadas = jogadas + 1
    computador1 = random.randint(0,fim)
    #gera um numero aleatorio de 0 ao fim
    n_adivinha = random.randint(0,fim)


    while computador1 != n_adivinha:
        cont = cont + 1
        n_adivinha = random.randint(inicio, fim)
        if n_adivinha < computador1 :
            inicio = n_adivinha
        if n_adivinha > computador1:
            fim = n_adivinha
    #print("O número é", computador1, "e o jogo foi jogado",cont,"vezes")
    soma = soma + cont
t1 = datetime.now()

media = soma/tentativas
print("A média de ",tentativas,"tentativas foi de",media)
print("Numero aleatorios de 0 a 1000")
print("Tempo de execução:",t1-t0)
