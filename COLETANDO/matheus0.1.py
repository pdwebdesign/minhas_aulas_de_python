import requests
import csv
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from openpyxl import Workbook


def coletando_acoes(page):
    page = requests.get(page)
    page = str(page.content)
    soup = BeautifulSoup(page,"html.parser")
    tabela = soup.find("table")
    tbody = tabela.find("tbody")
    lista_acoes = []

    for row in tbody.find_all("tr"):
        cells = row.find_all("td")
        acoes = cells[0].find(text=True)
        lista_acoes.append(acoes)
    return lista_acoes
    print(lista_acoes)
def coletando_precos(page,acao):
    page = requests.get(page)
    page = str(page.content)
    soup = BeautifulSoup(page, "html.parser")
    tabela = soup.find("table")
    tbody = tabela.find("tbody")
    tabela_data = []
    tabela_valor = []

    for row in tbody.find_all("tr"):
        cells = row.find_all("td")
        data = cells[0].find(text=True)
        valor = cells[5].find(text=True)
        tabela_data.append(data)
        tabela_valor.append(valor)

    df["Data"+acao] = tabela_data
    df["Preço"+acao] = tabela_valor
    return df

lista_total_acoes = []
numero = 0
i = 0
df = pd.DataFrame()
while numero < 10:
    numero = str(numero)
    completo = "https://finance.yahoo.com/lookup/equity?s=a&t=A&b=" + numero + "&c=100"
    total_acoes = coletando_acoes(completo)
    lista_total_acoes.extend(total_acoes)

    numero = int(numero)
    numero += 100
    #print(completo)

tamanho_lista = len(lista_total_acoes)
#print(lista_total_acoes)
#print(tamanho_lista)

while i < 10:
    acao = lista_total_acoes[i]
    print(acao)
    if acao == "AAPL" or acao == "HMNY" or acao == "T" or acao == "A" or acao == "AMAT":
        i += 1
    else:
        completo = "https://finance.yahoo.com/quote/" + acao + "/history?p=" + acao

        total_acoes = coletando_precos(completo, acao)
    i += 1
    #print(completo)
print("--------------PRINT FINAL--------------------")
print(df)
#total_acoes.read_csv('banco.csv', encoding='ISO-8859-1')
total_acoes.to_csv('banco.csv')
writer = pd.ExcelWriter('banco2.xlsx')
total_acoes.to_excel(writer)
writer.save()

