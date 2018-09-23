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

def cadastrarCategoria(nome):
    #adicionar o nome e o valor 0 para inicializar a categoria
    categorias.append([nome, 0])

def relatorioCategoria():
    #retornar nome e a quantidade de venda daquela categoria
    lista_categorias = ''
    for cat in categorias:
        lista_categorias += cat[0] + '\t' + str(cat[1]) + '\n'
    return lista_categorias

def cadastrarProduto(nome,preco,desc,categoria,qnt):
    pass

def listarProdutos():
    pass

def procurarId(i):
    pass

def procurarNome(nome):
    pass

def realizarVenda(lista_itens):
    pass

def converte():
    pass
        
def carrega():
    pass
    
def salva():
    pass




