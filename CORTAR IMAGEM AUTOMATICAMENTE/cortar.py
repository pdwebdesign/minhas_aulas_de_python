from PIL import Image

numColunas = 10
numLinhas = 8

caminhoImagem = "zelda.png"
img = Image.open(caminhoImagem)
tamanho = img.size
fator = tamanho[0]/numColunas
fatorTamanho = tamanho[1]/numLinhas

for i in range(0,numColunas):
    for j in range(0,numLinhas):
        #xInicial = (fator/2)+i*fator
        #xFinal = (fator/2)+(i+1)*fator
        imagemCortada = img.crop((i*fator,j*fatorTamanho,(i+1)*fator,((j+1)*(fatorTamanho))))
        nomeImagem ="img"+str(i)+str(j)+".png"
        imagemCortada.save(nomeImagem)