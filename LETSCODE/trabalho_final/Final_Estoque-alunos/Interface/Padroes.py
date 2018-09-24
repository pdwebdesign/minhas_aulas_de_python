import tkinter as tk
import tkinter.ttk as ttk

class buttonLets(tk.Button):
    def __init__(self,text=""):
        self.text = text


class TelaLets(tk.Tk):
    def __init__(self,tela):
        tela.tk_setPalette(background='#2c465b', foreground='#f4d039', activeBackground='#f4d039',
                           activeForeground="#2c465b",fieldbackground="#f4d039")
        style = ttk.Style(tela)
        # set ttk theme to "clam" which support the fieldbackground option
        style.theme_use("clam")
        style.configure("Treeview",background='#2c465b', foreground='#f4d039', activeBackground='#f4d039',
                        activeForeground="#2c465b",fieldbackground="#2c465b")