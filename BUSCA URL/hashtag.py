# -*- coding: utf-8 -*-
import requests

def get_page(page):#pega o html da pagina
    page = requests.get(page)
    #print(page)
    #print(page.status_code)  # 200 significa requisição OK
    page = str(page.content)
    return page

def get_next_target(page):
    start_link = page.find('#')
    if start_link == -1:
        return None, 0
    start_quote = page.find('#', start_link)#procura o # a partir
    end_quote = page.find(' ',start_quote + 1)
    palavra = page[start_quote + 1: end_quote]
    return palavra, end_quote

def print_all_links(page):
    palavras = []
    while True:
        palavra, endpos = get_next_target(page)
        if palavra:
            palavras.append(palavra)
            page = page[endpos:]
        else:
            break
    return palavras

palavra_escrita = input("Digite uma palavra\n")
palavra_escrita = palavra_escrita + "/"
page = get_page("https://www.instagram.com/explore/tags/" + palavra_escrita)

lista = print_all_links(page)

dicionario = {}
for i in range(0,len(lista)):
    dicionario[lista[i]] = lista.count(lista[i])

from collections import OrderedDict
dicionario_ordered = OrderedDict(sorted(dicionario.items(), key=lambda t: t[1]))

for k, v in dicionario_ordered.items():
    print(' {0} \t : {1}'.format(k,v))