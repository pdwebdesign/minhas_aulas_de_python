#Crie uma lista de strings com todos os meses do ano e solicite a entrada de um numerro de 1 a 12. Imprima o nome dos mês de acordo com o número digitado.

meses = ["janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
print(meses)
escolha = int(input("Digite um numero de 1 a 12"))
print(meses[escolha-1])

#EXERCICIO 3 SLIDE 1
vetor1 = [1,6,3,4,2]
vetor2 = [2,7,8,5,3]

vetor3 = [vetor1[0],vetor1[2],vetor1[1],vetor1[4],vetor1[3]]