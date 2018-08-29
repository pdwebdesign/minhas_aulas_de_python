#CONCEITO DE PROCESSO / FUNÇÃO
#EVITAR FAZER TUDO DE NOVO E DE NOVO À MÃO
#PODEMOS ESCREVER O CODIGO UMA VEZ E UTILIZAR VARIAS VEZES, MUDANDO ENTRADAS PARA GERAR DIFERENTES COMPORTAMENTOS.
import requests

page3 = requests.get('http://www.youtube.com')
print(page3)
print(page3.status_code)  # 200 significa requisição OK
page = str(page3.content)
def extrair_link(response):
    start_link = page.find("<a href=")
    start_aspas = page.find('"', start_link)
    end_aspas = page.find('"', start_aspas + 1)
    url = page[start_aspas + 1:end_aspas]
    return url,end_aspas
def resto_da_string(s,end):
    return s[end:]
while(page.find("<a href=") != -1):
    url, fim = extrair_link(page)
    page = resto_da_string(page,fim)
    print(url,fim)






