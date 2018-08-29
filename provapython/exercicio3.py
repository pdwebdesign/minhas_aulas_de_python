soma = 0
for i in range(0,3):
    nota = int(input("Digite nota\n"))
    soma = soma + nota
media = soma/3
total_aulas = int(input("Digite o numero total de aulas:\n"))
total_faltas = int(input("Digite o numero total de faltas:\n"))

print("A media do aluno é ",media)
if total_faltas > total_aulas * 0.25:
    print("O aluno foi reprovado por falta\n")
else:
    if media >= 7:
        print("Aluno aprovado!!")
    if media >=3 and media < 7:
        print("Aluno está de recuperação")
        nota_final = int(input("Digite a nota da prova de recuperação\n"))
        media_final =  (media + nota_final)/4
        if media_final >= 5:
            print("Aluno aprovado")
        else:
            print("Aluno reprovado")
    if media < 3:
        print("Aluno foi reprovado")

