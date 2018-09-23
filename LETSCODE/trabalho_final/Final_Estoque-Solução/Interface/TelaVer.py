import tkinter as tk
import tkinter.ttk as ttk
from Interface.Padroes import *


class TelaVer(TelaLets):
    def __init__(self, tela,listaItens):
        super(TelaVer,self).__init__(tela)
        tela.geometry("300x300")

        # Pegando lista
        self.listaItens = listaItens


        self.tree = ttk.Treeview(tela)

        self.tree["columns"] = ("Nome", "Valor")
        self.tree.column("#0", width=50)
        self.tree.column("Nome", width=100)
        self.tree.column("Valor", width=100)
        self.tree.heading("#0", text="Id")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Valor", text="Valor")

        self.tree.pack()
        self.inserirDados()

    def inserirDados(self):
        for i in range(len(self.listaItens)):
            item = [self.listaItens[i][0],self.listaItens[i][1]]
            self.tree.insert('','end',text=i,value=item)

