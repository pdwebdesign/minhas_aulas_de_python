import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

page_nexa = "https://finance.yahoo.com/quote/NEXA/history/"

page_nyse = "https://finance.yahoo.com/quote/%5ENYA/history?ltr=1"

page_nexa = requests.get(page_nexa)
page_nexa= str(page_nexa.content)

page_nyse = requests.get(page_nyse)
page_nyse= str(page_nyse.content)

soup_nexa = BeautifulSoup(page_nexa,"html.parser")
soup_nyse = BeautifulSoup(page_nyse,"html.parser")


all_tables_nexa = soup_nexa.find_all("table")
tabela_nexa = soup_nexa.find("table")

all_tables_nyse = soup_nyse.find_all("table")
tabela_nyse = soup_nyse.find("table")

tbody_nexa = tabela_nexa.find("tbody")
tbody_nyse = tabela_nyse.find("tbody")

tabela_data_nexa = []
tabela_valor_nexa = []
tabela_retorno_nexa = []
tabela_data_nyse = []
tabela_valor_nyse = []
tabela_retorno_nyse = []
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

for row in tbody_nyse.find_all("tr"):
    cells = row.find_all("td")
    data = cells[0].find(text=True)
    #valor_ant = valor
    valor = cells[5].find(text=True)
    #retorno = np.log(valor / valor_ant)
    tabela_data_nyse.append(data)
    tabela_valor_nyse.append(valor)
    #tabela_retorno_nyse.append(retorno)


df = pd.DataFrame()
df["Data Nexa"] = tabela_data_nexa
df["Preço Nexa"] = tabela_valor_nexa
df["Data Nyse"] = tabela_data_nyse
df["Preço Nyse"] = tabela_valor_nyse
print(df)