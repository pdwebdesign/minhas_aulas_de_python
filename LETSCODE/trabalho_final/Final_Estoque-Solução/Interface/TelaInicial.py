import tkinter as tk
from Interface.Padroes import *
from Interface.TelaAdd import *
from Interface.TelaRemove import *
from Interface.TelaVer import *
from Interface.TelaFiltro import *
from Interface.TelaContagem import *


class TelaInicial(TelaLets):
    def __init__(self,tela,listaItens):
        super(TelaInicial,self).__init__(tela)
        tela.geometry("300x300")

        #Pegando lista
        self.listaItens = listaItens

        #Frame
        frame = tk.Frame()
        frame.pack()
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

        #Botao
        botao1 = tk.Button(frame,text="Add Item",width=12,command=self.telaAdd)
        botao1.pack()

        # Botao
        botao2 = tk.Button(frame,text="Ver Itens",width=12,command=self.telaVer)
        botao2.pack()

        # Botao
        botao3 = tk.Button(frame,text="Remover Item",width=12,command=self.telaRemove)
        botao3.pack()

        # Botao
        botao4 = tk.Button(frame,text="Filtros",width=12,command=self.telaFiltros)
        botao4.pack()



    def telaAdd(self):
        tela2 = tk.Tk()
        TelaAdd(tela2,self.listaItens)
        tela2.mainloop()

    def telaVer(self):
        tela2 = tk.Tk()
        TelaVer(tela2,self.listaItens)
        tela2.mainloop()

    def telaRemove(self):
        tela2 = tk.Tk()
        TelaRemove(tela2,self.listaItens)
        tela2.mainloop()

    def telaFiltros(self):
        tela2 = tk.Tk()
        TelaFiltro(tela2,self.listaItens)
        tela2.mainloop()

    def telaContagem(self):
        tela2 = tk.Tk()
        TelaContagem(tela2,self.listaItens)
        tela2.mainloop()