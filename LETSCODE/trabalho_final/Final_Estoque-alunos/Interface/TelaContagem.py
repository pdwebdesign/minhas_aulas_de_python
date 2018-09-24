import tkinter as tk
from Interface.Padroes import *
from Funcoes.Funcoes import *

class TelaContagem(TelaLets):
    def __init__(self,tela,listaItens):
        super(TelaContagem, self).__init__(tela)
        tela.geometry("400x300")

        # Pegando lista
        self.listaItens = listaItens

        self.tree = ttk.Treeview(tela)

        self.tree["columns"] = ("Nome", "Valor","Quantidade")
        self.tree.column("#0", width=50)
        self.tree.column("Nome", width=100)
        self.tree.column("Valor", width=100)
        self.tree.column("Quantidade", width=100)
        self.tree.heading("#0", text="Id")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Valor", text="Valor")
        self.tree.heading("Quantidade", text="Quantidade")


        self.tree.pack()
        self.inserirDados()

    def inserirDados(self):
        listaContagem = contagem(self.listaItens)
        for i in range(len(listaContagem)-1):
            self.tree.insert('', 'end', text=i, value=self.listaContagem[i])

