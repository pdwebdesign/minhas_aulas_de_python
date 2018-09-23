from modulo import Macaco

macaco1 = Macaco('Simao')
macaco2 = Macaco('Prego')

macaco1.comer('Maca')
macaco1.verBucho()
macaco1.comer('Banana')
macaco1.verBucho()
macaco1.comer('Abacaxi')
macaco1.verBucho()
macaco1.digerir()
macaco1.verBucho()
macaco2.comer('Maca')
macaco2.comer('Banaca')
macaco2.comer(macaco1.nome)
macaco2.verBucho()
