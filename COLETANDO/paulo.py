import requests
import pandas as pd
import numpy as np

from bs4 import BeautifulSoup

page = "http://www.acinh.com.br/servicos/cotacao-dolar"

page = requests.get(page)
page = str(page.content)

soup = BeautifulSoup(page,"html.parser")

all_tables = soup.find_all("table")
nova_tabela = soup.find("table")


thead = nova_tabela.find("thead")
#print(nova_tabela)

#print(thead)

tabela_data = [10,20,30,40,50,60,70,80,90,100]
tabela_compra = []
tabela_venda = []

df = pd.DataFrame(tabela_data,columns=['Number'])
for row in thead.find_all("th"):
    valor = row.find(text=True)
    print(valor)
    df[valor] = tabela_data

print(df)


