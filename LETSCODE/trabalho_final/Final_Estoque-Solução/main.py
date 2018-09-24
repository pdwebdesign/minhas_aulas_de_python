import tkinter as tk
from Interface.TelaInicial import *
from Funcoes.IO import *


tela = tk.Tk()
tela.tk_setPalette(background='#2c465b', foreground='#f4d039', activeBackground='#f4d039', activeForeground="#2c465b")
listaItens = lerArquivo("saida.txt")

TelaInicial(tela,listaItens)
tela.mainloop()

salvandoArquivo("saida.txt",listaItens)
