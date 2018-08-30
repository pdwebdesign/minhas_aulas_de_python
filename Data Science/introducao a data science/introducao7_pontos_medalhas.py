#https://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html
#http://pandas.pydata.org/pandas-docs/stable/


import numpy
from pandas import DataFrame, Series


def points():
    '''

Imagine um sistema de pontos no qual cada país recebe 4 pontos por cada
    medalha de ouro, 2 pontos por cada medalha de prata e um ponto por cada
    medalha de bronze.

    Usando a função numpy.dot, crie um novo dataframe chamado
    'olympic_points_df' que inclui:
        a) uma coluna chamada 'country_name' com o nome do país
        b) uma coluna chamada 'pontos' com o número total de pontos do país
           ganhou nas Olimpíadas de Sochi.
    '''

    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

    olympic_medals_counts = {'country_name':Series(countries),'gold':Series(gold),
                             'silver':Series(silver),'bronze':Series(bronze)
                             }

    olympic_medals_counts_df = DataFrame(olympic_medals_counts)

    medal_counts = olympic_medals_counts_df[['gold','silver','bronze']]

    points = numpy.dot(medal_counts,[4,2,1])

    olympic_points = {'country_name':Series(countries),'points':Series(points)}

    olympic_points_df = DataFrame(olympic_points)

    print(olympic_points_df)

    return olympic_points_df

points()