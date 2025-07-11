class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcularPerimetro(self):
        return 2 * (self.largura + self.altura)

    def calcularArea(self):
        return round((self.largura * self.altura), 2)

retangulo1 = Retangulo(10, 20)
print(retangulo1.calcularPerimetro(), retangulo1.calcularArea())
