def testando(*posicional,**chavevalor):
	print("Posicional",posicional)
	print("Chavevalor",chavevalor)
	print()


testando(1,2,3)
testando(nome="maria",idade=18)
testando(1,2,3,4,5, nome="joao",idade=25)