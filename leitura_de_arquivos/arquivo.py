def ler_arquivo(a):
    try:
        print("arquivo lido")
        arquivo = open(a, 'r')
    except IOError as e:
        print(e)
        print("Criando o arquivo",e)
        arquivo = open(a, 'wt')

nome_arquivo = input("Digite o nome do arquivo")
ler_arquivo(nome_arquivo)


'''
arquivo = open("teste.txt","wt")
arquivo.write("OI\n")
arquivo.write("Teste")
arquivo.close()

arquivoLeitura = open("teste.txt","r")
for line in arquivoLeitura:
    print(str(line))

print(arquivoLeitura.read())
arquivoLeitura.close()
'''
