import tkinter as tk
from Interface.Padroes import *
from Funcoes.Funcoes import *

class TelaRemove(TelaLets):
    def __init__(self, tela,listaItens):
        self.tela = tela
        super(TelaRemove,self).__init__(self.tela)
        self.tela.geometry("150x200")

        # Pegando lista
        self.listaItens = listaItens

        variable = tk.StringVar(self.tela)
        variable.set("Opção")  # default value

        listaNomes = []
        for item in self.listaItens:
            listaNomes.append(item[0])

        menu = tk.OptionMenu(self.tela, variable,*listaNomes,command=self.removeItem)
        menu.pack()

    def removeItem(self,nome):
        removerItem(self.listaItens,nome)
        self.tela.destroy()



