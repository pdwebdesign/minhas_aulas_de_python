import requests
import numpy as np
import pandas
from bs4 import BeautifulSoup

#Falar d Try except
'''
    try:
        total_acoes = coletando_precos(completo, acao)
    except:
        print("-------!!!!erro na acao:!!!!-------", acao)
'''

'''
O código anterior não pegava quando a string vinha como 1.456,76 dessa forma eu troquei tudo que é ponto em espaço vazio e tudo que é virgula em ponto dai fiz transformar em float:
Linha 50:
valor = valor.replace(".","").replace(",",".")
'''

