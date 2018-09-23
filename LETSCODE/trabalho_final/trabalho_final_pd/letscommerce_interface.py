import letscommerce as lc
from tkinter import *
from tkinter import messagebox

def janCadastro():
    jan = Toplevel()
    Label(jan,text='Nome:',anchor='w').pack(fill=X,padx=10)
    nome = StringVar()
    Entry(jan,textvariable = nome,).pack(fill=X,padx=10,pady=5)
    Label(jan,text='Preço:',anchor='w').pack(fill=X,padx=10)
    preco = StringVar()
    Entry(jan,textvariable = preco,).pack(fill=X,padx=10,pady=5)
    Label(jan,text='Descrição:',anchor='w').pack(fill=X,padx=10)
    desc = StringVar()
    Entry(jan,textvariable = desc,).pack(fill=X,padx=10,pady=5)
    Label(jan,text='Categoria:',anchor='w').pack(fill=X,padx=10)
    cat = StringVar()
    opt = []
    for prod in lc.categorias:
        opt.append(prod[0])
    if len(opt)==0:
        opt.append('')
    OptionMenu(jan,cat,*opt).pack(fill=X,padx=10,pady=5)
    Label(jan,text='Quantidade:',anchor='w').pack(fill=X,padx=10)
    qnt = StringVar()
    Entry(jan,textvariable = qnt,).pack(fill=X,padx=10,pady=5)
    Button(jan,text='Cadastrar',command=lambda:(messagebox.showinfo("Cadastro",lc.cadastrarProduto(nome.get(),float(preco.get()),desc.get(),cat.get(),int(qnt.get()))),jan.destroy())).pack(fill=X,padx=10,pady=5)

def janQualquer(titulo,string):
    jan = Toplevel()
    Label(jan,text=titulo).pack(fill=X,padx=10,pady=5)
    Label(jan,text=string).pack(fill=X,padx=10,pady=5)

venda_atual = []
def vendaUpdate(nome,qnt,itens):
    prod = lc.procurarNome(nome)
    if len(prod) > 0:
        venda_atual.append([prod[0],int(qnt)])
        s = ''
        for i in venda_atual:
            s += lc.procurarId(i[0])[1] + '\t' + str(qnt) + '\n'
        itens.set(s)
        
def janVendas():    
    global venda_atual
    venda_atual = []
    jan = Toplevel()
    opt = []
    for prod in lc.produtos:
        opt.append(prod[1])
    if len(opt)==0:
        opt.append('')
    nome = StringVar()
    nome.set('Produtos:')
    OptionMenu(jan,nome,*opt).pack(fill=X,padx=10,pady=5)
    Label(jan,text='Quantidade:').pack(fill=X,padx=10,pady=5)
    qnt = StringVar()
    Entry(jan,textvariable = qnt).pack(fill=X,padx=10,pady=5)
    itens = StringVar()
    Button(jan,text='Adicionar Item',command=lambda:vendaUpdate(nome.get(),int(qnt.get()),itens)).pack(fill=X,padx=10,pady=5)
    Button(jan,text='Realizar Venda',command=lambda:(messagebox.showinfo("Venda",lc.realizarVenda(venda_atual)),jan.destroy())).pack(fill=X,padx=10,pady=5)
    Label(jan,text='Itens: ').pack(fill=X,padx=10,pady=5)
    Label(jan,textvariable=itens,height = 5,background='#1c364b' ).pack(fill=X,padx=10,pady=5)
    
def janCategoria():
    jan = Toplevel()
    var = StringVar()
    Label(jan,text='Nome da Categoria:',anchor='w').pack(fill=X,padx=10,pady=5)
    Entry(jan,textvariable = var,).pack(fill=X,padx=10,pady=5)
    Button(jan,text='Cadastrar',command=lambda:(lc.cadastrarCategoria(var.get()),jan.destroy())).pack(fill=X,padx=10,pady=5)
try:
    lc.carrega()
except:
    lc.salva()

root = Tk()
root.tk_setPalette(background='#2c465b', foreground='#f4d039', activeBackground='#f4d039', activeForeground="#2c465b")
root.option_add("*font", ("Verdana", 12))
root.winfo_toplevel().title("Let's Code Academy")

Label(root,text="Let's\nCommerce",font=('Arial',25,('italic','bold'))).pack(fill=X,padx=10,pady=5)

Button(root,text='Cadastrar Produto',command=janCadastro).pack(fill=X,padx=10,pady=5)
Button(root,text='Cadastrar Categoria',command=janCategoria).pack(fill=X,padx=10,pady=5)
Button(root,text='Realizar Venda',command=janVendas).pack(fill=X,padx=10,pady=5)
Button(root,text='Relatório Vendas',command=lambda: janQualquer('Vendas',lc.relatorioVendas())).pack(fill=X,padx=10,pady=5)
Button(root,text='Relatório Categorias',command=lambda: janQualquer('Vendas por Categoria',lc.relatorioCategoria())).pack(fill=X,padx=10,pady=5)

root.mainloop()
lc.salva()
