import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


def coletando(page_nexa):

    page_nexa = requests.get(page_nexa)
    page_nexa= str(page_nexa.content)

    soup_nexa = BeautifulSoup(page_nexa,"html.parser")

    all_tables_nexa = soup_nexa.find_all("table")
    tabela_nexa = soup_nexa.find("table")

    tbody_nexa = tabela_nexa.find("tbody")

    tabela_data_nexa = []
    tabela_valor_nexa = []
    tabela_retorno_nexa = []

    valor = 0
    valor_ant = 0
    retorno = 0

    for row in tbody_nexa.find_all("tr"):
        cells = row.find_all("td")
        data = cells[0].find(text=True)
        #valor_ant = valor
        valor = cells[5].find(text=True)
        #retorno = np.log(valor/valor_ant)
        tabela_data_nexa.append(data)
        tabela_valor_nexa.append(valor)
        #tabela_retorno_nexa.append(retorno)
    df = pd.DataFrame()
    df["Data Nexa"] = tabela_data_nexa
    df["Preço Nexa"] = tabela_valor_nexa
    print(df)

def coletando_links():
    link_completo = "https://finance.yahoo.com/quote/ACAD/history?p=ACAD"



#page = ["https://finance.yahoo.com/quote/NEXA/history/"]
#lista_name = ["PETR4.SA","NEXA",]
#coletando(page[0])
numero = 25
while numero < 90000:
    numero = str(numero)
    completo = "https://finance.yahoo.com/lookup/all?s=a&t=A&b=+"+numero+"&c="+numero
    coletando(completo)



    numero = int(numero)
    numero += 25
    print(completo)
