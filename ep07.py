class Carro:

    def __init__(self, consumo, combustivel=0):
        self.consumo = consumo
        self.combustivel = combustivel
    
    def andar(self, distancia):
        self.combustivel -= (distancia / self.consumo)
    
    def exibirCombustivel(self):
        print(f"{self.combustivel:.1f}")
    
    def abastecer(self, litros):
        self.combustivel += litros

meuCarro = Carro(12)
meuCarro.abastecer(40)
meuCarro.exibirCombustivel
meuCarro.andar(160)
meuCarro.exibirCombustivel()
meuCarro.andar(280)
meuCarro.exibirCombustivel()
