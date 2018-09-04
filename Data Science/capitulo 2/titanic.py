import numpy
import pandas
import statsmodels.api as sm


def simple_heuristic(file_path):
    '''
    Sua previsão deve ser 78% precisa ou superior.
        
    Aqui está uma heurística simples para começar:
       1) Se o passageiro é do sexo feminino, sua heurística deve assumir que o
       passageiro sobreviveu.
       2) Se o passageiro é do sexo masculino, sua heurística deve
       suponha que o passageiro não sobreviveu.
    
    Você pode acessar o gênero de um passageiro via passageiro ['Sex'].
    Se o passageiro for do sexo masculino, o passageiro ['Sex'] retornará uma string "macho".
    Se o passageiro for do sexo feminino, o passageiro ['Sex'] retornará uma string "female".

    Escreva sua previsão de volta no dicionário "previsões". o
    A chave do dicionário deve ser o id do passageiro (que pode ser acessado
    via passageiro ["PassengerId"]) eo valor associado deve ser 1 se o
    passageiro sobreviveu ou 0 caso contrário.

    Por exemplo, se for previsto que um passageiro tenha sobrevivido:
    passageiro_id = passageiro ['PassengerId']
    previsões [passenger_id] = 1

    E se for previsto que um passageiro tenha morrido no desastre:
    passageiro_id = passageiro ['PassengerId']
    previsões [passenger_id] = 0
    '''

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']


    return predictions
