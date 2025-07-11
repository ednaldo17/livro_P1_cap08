class Calculadora:

    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def somar(self):
        return self.op1 + self.op2

    def subtrair(self):
        return self.op1 - self.op2

    def multiplicar(self):
        return round((self.op1 * self.op2), 2)
    
    def dividir(self):
        return round((self.op1 / self.op2), 2)
    
    def calcularPotencia(self):
        return round((self.op1 ** self.op2), 2)

teste1 = Calculadora(7, 5)
print(teste1.somar())
print(teste1.subtrair())
print(teste1.multiplicar())
print(teste1.dividir())
print(teste1.calcularPotencia())
