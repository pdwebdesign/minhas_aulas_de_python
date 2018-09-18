import requests

from bs4 import BeautifulSoup

page = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

page = requests.get(page)
page = str(page.content)



#Parseia o html na variável 'page', e armazena em formato Beautiful Soup
soup = BeautifulSoup(page)

print(soup.title)