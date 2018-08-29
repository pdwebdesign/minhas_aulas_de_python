#EXERCICIO DA PRIMEIRA OU SEGUNDA AULA PARA CASA
page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="lets float-left"> <a href="http://www.letscode-academy.com">'''

start_link = page.find("<a href=")
start_aspas = page.find('"',start_link)
end_aspas = page.find('"',start_aspas + 1)

url = page[start_aspas + 1:end_aspas]

print(url)