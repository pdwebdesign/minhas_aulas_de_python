import tkinter as tk
from Interface.Padroes import *
from Funcoes.Funcoes import *

class TelaAdd(TelaLets):
    def __init__(self,tela,listaItens):
        super(TelaAdd,self).__init__(tela)
        self.tela = tela
        tela.geometry("200x200")

        # Pegando lista
        self.listaItens = listaItens

        #Frame
        frame = tk.Frame(tela)
        frame.pack()
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

        labelNome = tk.Label(frame,text="Nome")
        labelNome.grid(row=0,column=0)

        self.entradaNome = tk.Entry(frame)
        self.entradaNome.grid(row=0,column=1)

        labelPreco = tk.Label(frame, text="Preço")
        labelPreco.grid(row=1, column=0)

        self.entradaPreco= tk.Entry(frame)
        self.entradaPreco.grid(row=1, column=1)

        botaoSalvar = tk.Button(frame,text="Salvar",command=self.addItem)
        botaoSalvar.grid(row=2, column=1)

    def addItem(self):
        nome = self.entradaNome.get()
        preco = self.entradaPreco.get()
        addItem(self.listaItens,nome,preco)
        self.tela.destroy()