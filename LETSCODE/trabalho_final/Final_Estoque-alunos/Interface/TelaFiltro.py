import tkinter as tk
from Interface.Padroes import *
from Funcoes.Funcoes import *

class TelaFiltro(TelaLets):
    def __init__(self,tela,listaItens):
        super(TelaFiltro,self).__init__(tela)
        self.tela = tela
        tela.geometry("300x400")

        # Frame
        self.frame = tk.Frame(tela)
        self.frame.pack()
        self.frame.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        frame1 = tk.Frame(self.frame)
        frame1.grid(row=0,column=0)

        frame2 = tk.Frame(self.frame)
        frame2.grid(row=1, column=0)

        labelNome = tk.Label(frame1,text="Nome",width=5)
        labelNome.pack(side=tk.LEFT)

        self.entradaNome = tk.Entry(frame1)
        self.entradaNome.pack(side=tk.LEFT)

        labelValor = tk.Label(frame2,text="Valor",width=5)
        labelValor.pack(side=tk.LEFT)

        self.entradaValor = tk.Entry(frame2)
        self.entradaValor.pack(side=tk.LEFT)

        botao = tk.Button(self.frame,text="Pesquisar",command=self.pesquisar)
        botao.grid(row=3,column=0)

        # Pegando lista
        self.listaItens = listaItens

    def pesquisar(self):
        # Frame
        self.frame2 = tk.Frame(self.tela)
        self.frame2.pack()
        self.frame2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.tree = ttk.Treeview(self.frame2)

        self.tree["columns"] = ("Nome", "Valor")
        self.tree.column("#0", width=50)
        self.tree.column("Nome", width=100)
        self.tree.column("Valor", width=100)
        self.tree.heading("#0", text="Id")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Valor", text="Valor")

        self.tree.grid(row=4, column=0)
        self.inserirDados()

    def inserirDados(self):
        nome = self.entradaNome.get()
        valor = self.entradaValor.get()
        listaFiltro = filtro(self.listaItens,nome,valor)
        for i in range(len(listaFiltro)):
            item = listaFiltro[i]
            self.tree.insert('', 'end', text=i, value=item)

