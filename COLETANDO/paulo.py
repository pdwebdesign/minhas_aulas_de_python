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

tabela_ano = []
tabela_mes = []
tabela_compra = []
tabela_venda = []


for row in thead.find_all("th"):
    if len(row) > 0:
        valor_ano = row.find(text=True)
        tabela_ano.append(valor_ano)

for row in nova_tabela.find_all("tr"):
    cells = row.find_all("td", class_="td-destaque")
    if len(cells) > 0:
        valor_mes = cells[0].find(text=True)
        tabela_mes.append(valor_mes)

for row in nova_tabela.find_all("tr"):
    cells_dados = row.find_all("td")
    for numero_coluna in range(1, 18):
        if len(cells_dados) > 10:
            valor = cells_dados[numero_coluna].find(text=True)
            if numero_coluna % 2 == 0:
                tabela_venda.append(valor)
            else:
                tabela_compra.append(valor)

tabela_data = []

for num_ano in range(0, len(tabela_ano) - 1):
    for num_mes in range(0, len(tabela_mes) - 1):
        index_data = tabela_ano[num_ano] + tabela_mes[num_mes]
        print(index_data)
        #tabela_data.append(index_data)