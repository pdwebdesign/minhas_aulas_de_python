from pandas import DataFrame,Series


def create_dataframe():
    cidades = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    ouro = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    prata = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]


    medalhas = {'cidades':Series(cidades),'ouro':Series(ouro),
                            'silver':Series(prata),'bronze':Series(bronze)}

    medalhas_df = DataFrame(medalhas)

    return medalhas_df

df = create_dataframe()

#print(df['cidades'])
#print(df[['cidades','bronze']])
#APENAS A LINHA
#print(df.loc[0])
#print(df.loc[4:10])

#condicoes:
#print(df[df['bronze']>=9])
#print("PEGAR OURO MAS APENAS QUE O BRONZE FOR MAIOR QUE 9")
print(df['ouro'][df['bronze']>=9])


