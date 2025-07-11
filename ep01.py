class Ingresso:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
    
    def exibirValor(self):
        return self.valor

    def __str__(self):
        return f"{self.nome}: {self.valor}"
    
ingresso1 = Ingresso("Rock n'Rio", 1500)
ingresso2 = Ingresso("Lollapalloza", 1260)
print(ingresso1.exibirValor())
print(ingresso2.exibirValor())
print(ingresso1)
print(ingresso2)
