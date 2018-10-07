import requests
import numpy as np
import pandas
from bs4 import BeautifulSoup

#RECUPERANDO AS INFORMACOES DO PANDA
#print(df["nome_da_coluna"])

df = pandas.read_csv('banco3.csv',encoding='ISO-8859-1')
#criar uma nova coluna trabalhando com panda
#print(df)
print(df["Preço AMZN"])
print(df["Preço AMD"])
df["acao soma"] = df["Preço AMZN"] + df["Preço AMD"]
print(df["acao soma"])
df.to_csv("soma.csv",encoding='ISO-8859-1')
writer = pandas.ExcelWriter('soma.xlsx')
df.to_excel(writer)
writer.save()

# array_1 = np.array([1, 2, 3], float)
# series = pandas.Series()
# series["Instructor"] = array_1
# series["Curriculum Manager"] = array_1
# print(series)
# series["soma"] = series["Instructor"] + series['Curriculum Manager']
# print(series)

