'''
Agora que sabemos um pouco sobre a manipulação de dados
vamos falar como vamos armazená-los e fazer referência
a eles usando Pandas
Os dados em Pandas geralmente são contidos em uma estrutura
chamada Dataframe
'''

'''
Dataframe é uma estrutura de dados bidimensionais organizada
em linhas e colunas. As colunas podem representar dados 
de diferente tipos , se necessário
'''

'''
dataframe é como se fosse uma planilha do excel
'''

import pandas as pd

'''
Você pode pensar em Series como um objeto unidimensional que é semelhante a
uma matriz, lista ou coluna em um banco de dados. Por padrão, ele atribuirá um
rótulo de índice para cada item da Série variando de 0 a N, onde N é
o número de itens da série menos um.
'''
# Change False to True to create a Series object
if False:
    series = pd.Series(['Dave', 'Cheng-Han', 'Udacity', 42, -1789710578])
    print(series)

'''
Você também pode atribuir manualmente os índices aos itens da Série quando
criando a série
'''

# Change False to True to see custom index in action
if False:
    series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
                       index=['Instructor', 'Curriculum Manager',
                              'Course Number', 'Power Level'])
    print(series)

'''
Você pode usar o índice para selecionar itens específicos da série
'''
# Change False to True to see Series indexing in action
if False:
    series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
                       index=['Instructor', 'Curriculum Manager',
                              'Course Number', 'Power Level'])
    print(series['Instructor'])
    print("")
    print(series[['Instructor', 'Curriculum Manager', 'Course Number']])

'''
Você também pode usar operadores booleanos para selecionar itens específicos da série
'''
# Change False to True to see boolean indexing in action
if False:
    cuteness = pd.Series([1, 2, 3, 4, 5], index=['Cockroach', 'Fish', 'Mini Pig',
                                                 'Puppy', 'Kitten'])
    print(cuteness > 3)
    print("")
    print(cuteness[cuteness > 3])

