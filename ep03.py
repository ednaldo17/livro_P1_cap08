class Ponto:
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.nome}: ({self.x}, {self.y})"

ponto1 = Ponto("Ponto 1", 10, -5)
print(ponto1)
