pessoas = []
for i in range(0, 5):
    pessoa = []
    pessoa.append(input('Informe a idade da pessoa: '))
    pessoa.append(input('Informe a altura da pessoa: '))
    pessoas.append(pessoa)

pessoas.reverse()
for pessoa in pessoas:
    print('Idade: %s - Altura: %s' % (pessoa[0], pessoa[1]))
