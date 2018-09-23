'''
for VAR in ARRAY
        BLOCK
'''
#TOMADA DE DECISAO DENTRO DO FOR
'''anos = [2015,2016,2017,2018]
for var in anos:
        if var % 2 == 0:
            print(var)'''

#5.1 CONCEITO DE BREAK DE UM LOOP
nomes = ['luiz da silva', 'fabio henrique', 'manoel de oliveira', 'jose maria de souza', 'antonio arruda', 'joaquim barbosa', 'maria da penha']

for nome in nomes:
        if nome.find('maria') > -1:
            nome_encontrado = nome
            print(nome_encontrado)

            

#COM O USO DO BREAK ELE ENCONTRA O PRIMEIRO NOME E NAO PROCURA MAIS OS OUTROS RETIRE O BREAK E VEJA O QUE ACONTECE

#LOOP TIPO WHILE
