site = "somos todos muito trabalhadores #amor #love , boa tarde"
pos = site.find("#")
if pos == -1:
    print("nao tem #")
esp = site.find(" ",pos)
palavra = site[pos + 1:esp]
print(palavra)
site = site[esp:]
print(site)
