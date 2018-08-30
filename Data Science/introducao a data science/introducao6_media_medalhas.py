import numpy
from pandas import DataFrame, Series


def avg_medal_count():
    '''
    Usando o método apply do dataframe, crie uma nova série chamada
    avg_medal_count que indica o número médio de ouro, prata,
    e medalhas de bronze ganhas entre os países que ganharam em
    menos uma medalha de qualquer tipo nas Olimpíadas de Sochi de 2014. Observe que
    a lista de países já inclui apenas países que ganharam
    pelo menos uma medalha. Nenhuma filtragem adicional é necessária.
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

    olympic_medal_counts = {'country_name': countries,
                            'gold': Series(gold),
                            'silver': Series(silver),
                            'bronze': Series(bronze)}
    olympic_medal_counts_df = DataFrame(olympic_medal_counts)

    avg_medal_counts = olympic_medal_counts_df[['gold','silver','bronze']].apply(numpy.mean)

    print(avg_medal_counts)

    return avg_medal_count

avg_medal_count()
