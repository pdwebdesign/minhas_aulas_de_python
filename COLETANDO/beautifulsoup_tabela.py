import requests
import pandas as pd

from bs4 import BeautifulSoup

page = "http://www.yahii.com.br/dolar.html"

page = requests.get(page)
page = str(page.content)

soup = BeautifulSoup(page,"html.parser")
'''
print(soup.title)
print(soup.title.string)

print(soup.a)
print(soup.find_all("a"))
'''
all_links = soup.find_all("a")
for link in all_links:
    link.get("href")

all_tables = soup.find_all('table')
nova_tabela = soup.find('table')
print(all_tables[4])
'''
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]

for row in nova_tabela.find_all("tr"):
    cells = row.find_all("td")
    h = row.find_all("th")
    if len(cells)==6:
        A.append(cells[0].find(text=True))
        B.append(h[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))
# print(A)
# print(B)
# print(C)
# print(D)
# print(E)
# print(F)
# print(G)

df = pd.DataFrame(A,columns=['Number'])
df['State']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
print(df)
'''