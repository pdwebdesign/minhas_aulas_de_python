#AULA 3 exercicio 1 temperaturas

def escala_temperatura(temperatura,valor):
   if temperatura == "k" or temperatura == "K":
       print("O valor ",valor,"em Kelvin é em\n")
       c = valor -273
       print("Celsius: ",c)
       f = float(1.8 * (valor - 273) + 32)
       print("Fahrenheit: ", f)
   if temperatura == "" or temperatura == "K":
       c = valor - 273
       print("Valor em Celsius: ", c)
   if temperatura == "k" or temperatura == "K":
       c = valor - 273
       print("Valor em Celsius: ", c)


temperatura = input("digite a escala da temperatura:\n")
valor = int(input("digite o valor da temperatura:\n"))

escala_temperatura(temperatura,valor)