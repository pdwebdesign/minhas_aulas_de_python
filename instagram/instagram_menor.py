# -*- coding: utf-8 -*-
import requests

palavra_recebida = input("Digite uma palavra")
palavra_escrita = palavra_recebida + "/"
page = "https://www.instagram.com/explore/tags/"+palavra_escrita

page = requests.get(page)
print(page.status_code)
page = str(page.content)


palavras = []
while True:
    inicio_palavra = page.find('#')
    if inicio_palavra == -1:
        break

    fim_palavra = page.find(' ', inicio_palavra)
    palavra = page[inicio_palavra + 1:fim_palavra]

    palavras.append(palavra)

    page = page[fim_palavra:]

    print(palavra)