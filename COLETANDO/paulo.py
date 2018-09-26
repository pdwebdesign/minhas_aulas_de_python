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
    numero_coluna = 1
    cells_dados = row.find_all("td")
    while numero_coluna <= 18:
        if len(cells_dados) > 10:
            valor = cells_dados[numero_coluna].find(text=True)
            if numero_coluna % 2 == 0:
                tabela_venda.append(valor)
            else:
                tabela_compra.append(valor)

        numero_coluna += 1
print(tabela_compra)
print(tabela_venda)