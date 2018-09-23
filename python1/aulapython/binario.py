bin = ""
decimal = 217
while (decimal >= 0):
  if decimal % 2 == 0:
    bin = "0" + bin
  else:
    bin = "1" + bin
  decimal = decimal / 2
  round(decimal)
print(bin)




