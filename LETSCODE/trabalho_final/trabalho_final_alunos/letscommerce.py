"""
Projeto LetsCommerce

Funções Principais:
    Cadastrar Produto
        cadastrarProduto(nome,preco,desc,categoria,qnt)
        retorno "String"
    Listar Produtos
        listarProdutos()
        retorno 'String'
    Realizar venda
        realizarVenda([[id,qnt]])
        retorno "String"
    Cadastrar Categoria
        cadastrarCategoria(nome)
        retorno "String"
    Editar Produto
        editarProduto(id,[produto])
        retorno [Produto Atualizado]
    Relatório de Vendas Por Categoria
        relatorioCategoria()
        retorno "Relatório"

Funções auxiliares:
    Procurar produto por nome
        procurarNome(nome)
        retorno [Produto]
    Procurar produto por id
        procurarId(id)
        retorno [Produto]

Dados:
    Produto:
        - id
        - Nome
        - Preço
        - Descrição
        - Categoria
        - Quantidade em Estoque

    Venda:
        - Preço Total da Venda
        - Lista de Produtos Vendidos
        - Forma de Pagamento

    Categorias:
        - Nome
        - Quantidade de itens vendidos
"""
import csv

produtos = []
vendas = []
categorias = []
id_atual = 0

def cadastrarProduto(nome,preco,desc,categoria,qnt):
    global id_atual, produtos,categorias
    existe = False
    for cat in categorias:
        if cat[0] == categoria:
            existe = True
    if not existe:
        return "Categoria não existente"
    
    produto = [id_atual,nome,preco,desc,categoria,qnt]
    produtos.append(produto)
    id_atual += 1
    return "Produto cadastrado com sucesso"

### Teste de cadastro de categorias   
##categorias.append(['a',0])
##cadastrarProduto('b',1.2,'aa','a',10)
##print(cadastrarProduto('c',10.50,'cc','a',5))
##print(cadastrarProduto('b',1.2,'aa','b',10))


def listarProdutos():
    s = ''
    for prod in produtos:
        s+=prod[1]+'\t'+prod[3]+'\t'+str(prod[2])+'\n'
    return s

def procurarId(i):
    p = []
    for prod in produtos:
        if prod[0] == i:
            p = prod
    return p

def procurarNome(nome):
    p = []
    for prod in produtos:
        if prod[1] == nome:
            p = prod
    return p

def realizarVenda(lista_itens):
    global categorias, produtos
    total = 0
    for item in lista_itens:
        prod = procurarId(item[0])
        #print('prod: ',prod)
        if len(prod)>0:
            for cat in categorias:
                #print('cat: ',cat)
                if cat[0]==prod[4]:
                    #print('categoria encontrada:',cat)
                    cat[1] += item[1]*prod[2]
                    total += item[1]*prod[2]
    if total > 0:
        vendas.append([total,lista_itens])
        return 'Venda Realizada'
    else:
        return 'Erro na venda'

def cadastrarCategoria(nome):
    global categorias
    categorias.append([nome,0])

def relatorioCategoria():
    s = ''
    for cat in categorias:
        s += cat[0] + '\t' +str(cat[1])+'\n'
    return s

def converte():
    for item in produtos:
        item[0] = int(item[0])
        item[2] = float(item[2])
        item[5] = int(item[5])
    for item in vendas:
        for x in item[1]:
            x[0] = int(x[0])
            x[1] = int(x[1])
    for cat in categorias:
        cat[1] = int(cat[1])
        
def carrega():
    global produtos,vendas,categorias
    produtos = []
    vendas = []
    categorias = []
    
    file = open('produtos.csv','r',encoding='utf8')
    rd = csv.reader(file)
    for row in rd:
        produtos.append(row)
    file.close()

    file = open('vendas.csv','r',encoding='utf8')
    rd = csv.reader(file)
    for row in rd:
        vendas.append(row)
    file.close()

    file = open('categorias.csv','r',encoding='utf8')
    rd = csv.reader(file)
    for row in rd:
        categorias.append(row)
    file.close()
    converte()
    
def salva():
    file = open('categorias.csv','w',encoding='utf8')
    wt = csv.writer(file,lineterminator='\n')
    wt.writerows(categorias)
    file.close()

    file = open('vendas.csv','w',encoding='utf8')
    wt = csv.writer(file,lineterminator='\n')
    wt.writerows(vendas)
    file.close()

    file = open('produtos.csv','w',encoding='utf8')
    wt = csv.writer(file,lineterminator='\n')
    wt.writerows(produtos)
    file.close()




