#EXERCICIO DA PRIMEIRA OU SEGUNDA AULA PARA CASA
page = '''Amarantina - 2 praça;Itabira - 2 praça;Mariana - 2 praça;Amanda - 2 praça;Itabira - 2 praça;Mariana - 2 praça;Amanda - 2 praça'''

municipio_inicio = 0
municipio_fim = page.find(" - 2 praça")
municipio = page[municipio_inicio:municipio_fim]
print(municipio)
while municipio_fim + 10 < len(page):
    municipio_inicio = page.find(';',municipio_fim)
    municipio_fim = page.find(" - 2 praça",municipio_inicio)
    municipio = page[municipio_inicio + 1:municipio_fim]
    print(municipio)

