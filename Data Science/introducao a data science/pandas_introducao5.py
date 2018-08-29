import pandas as pd

'''

Você pode pensar em um DataFrame como um grupo de séries que compartilham um índice.
Isso facilita a seleção de colunas específicas que você deseja do
Quadro de dados.

Também alguns pontos:
1) Selecionando uma única coluna do DataFrame retornará uma série
2) Selecionar várias colunas do DataFrame retornará um DataFrame
'''
# Change False to True to see Series indexing in action
if True:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print("football['year']")
    print(football['year'])
    print("football.year")
    print(football.year)
    print("football[['year', 'wins', 'losses']]")
    print(football[['year', 'wins', 'losses']])

'''

A seleção de filas pode ser feita de várias maneiras.

Alguns dos métodos básicos e comuns são:
   1) Fatiar
   2) Um índice individual (através das funções iloc ou loc)
   3) indexação booleana

Você também pode combinar vários requisitos de seleção por meio de
operadores como & (and) ou | (or)
'''
# Change False to True to see boolean indexing in action
if True:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print("\nfootball.iloc[[7]]-o ultimo termo é excluido\n")
    print(football.iloc[:5])
    print("\nfootball.loc[[7]]\n")
    print(football.loc[:5])
    print("\nfootball[3:5]\n")
    print(football[3:5])
    print("\nfootball[football.wins > 10]\n")
    print(football[football.wins > 10])
    print('\nfootball[(football.wins > 10) & (football.team == "Packers")]\n')
    print(football[(football.wins > 10) & (football.team == "Packers")])