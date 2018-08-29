nomes = ["Paulo Pedro #amordenovela #Rogerio ","#Neymar","PedroSon","Paulo Pedro #amordenovela ","Rogerio","#Neymar","PedroSon"]

texto = nomes[0]


inicio = texto.find('#')
texto_cortado = texto[inicio+1:]

fim = texto_cortado.find(' ')

print(texto_cortado[:fim])
