class Veiculo(object):

    def __init__(self,posicao,velocidade):
        self.posicao = posicao
        self.velocidade = velocidade
    def andar(self,velocidade,posicao,tempo):
         self.distancia_final = posicao + (velocidade * tempo)


class Moto(Veiculo):
    def __init__(self,posicao,velocidade):
        self.velocidade = velocidade
    def andar(self,velocidade,posicao,tempo):
         self.distancia_final = posicao + (velocidade * tempo)