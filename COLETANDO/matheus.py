import requests
import numpy
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

tbody = tabela_nexa.find("tbody")
#print(tbody)

tabela_data = []
tabela_valor = []

df = pd.DataFrame(tabela_data,columns=['Number'])
for row in tbody.find_all("tr"):
    cells = row.find_all("td")
    data = cells[0].find(text=True)
    valor = cells[5].find(text=True)
    print(data)
    print(valor)


#print(df)