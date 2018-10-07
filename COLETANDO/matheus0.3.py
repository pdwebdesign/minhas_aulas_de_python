import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

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

def coletando_precos(page, acao):
    page = requests.get(page)
    page = str(page.content)
    soup = BeautifulSoup(page, "html.parser")
    tabela = soup.find("table")
    tbody = tabela.find("tbody")
    cont = 0
    valor = 1
    tabela_data = []
    tabela_valor = []
    tabela_retorno = []
    for row in tbody.find_all("tr"):
        cells = row.find_all("td")
        valor_ant = valor
        data = cells[0].find(text=True)
        valor = cells[5].find(text=True)
        valor = valor.replace(".","").replace(",",".")
        valor = float(valor)
        retorno = np.log(valor_ant / valor)
        tabela_data.append(data)
        tabela_valor.append(valor)
        if cont > 0:
            tabela_retorno.append(retorno)
        cont += 1
    tabela_retorno.append(" ")
    df["Data "+ acao] = tabela_data
    df["Preço " + acao] = tabela_valor
    df["Retorno " + acao] = tabela_retorno
    return df

lista_total_acoes = []
numero = 0
i = 0
df = pd.DataFrame()
while numero < 100:
    numero = str(numero)
    completo = "https://finance.yahoo.com/lookup/equity?s=a&t=A&b=" + numero + "&c=100"
    total_acoes = coletando_acoes(completo)
    lista_total_acoes.extend(total_acoes)
    numero = int(numero)
    numero += 100

tamanho_lista = len(lista_total_acoes)

while i < 100:
    acao = lista_total_acoes[i]
    print(acao)

    completo = "https://finance.yahoo.com/quote/" + acao + "/history?p=" + acao
    try:
        total_acoes = coletando_precos(completo, acao)
    except:
        print("-------!!!!erro na acao:!!!!-------", acao)
    print(total_acoes)
    i += 1

writer = pd.ExcelWriter('banco2.xlsx')
total_acoes.to_excel(writer)
writer.save()
total_acoes.to_csv('banco.csv',encoding='ISO-8859-1')
