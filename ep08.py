class ContaInvestimento:

    def __init__(self, saldo, taxaJuros):
        self.saldo = saldo
        self.taxaJuros = taxaJuros
    
    def adicionarJuros(self):
        self.saldo += self.saldo * self.taxaJuros / 100
    
conta1 = ContaInvestimento(1000, 10)
print(conta1.saldo)
conta1.adicionarJuros()
print(conta1.saldo)
conta1.adicionarJuros()
print(conta1.saldo)
conta1.adicionarJuros()
print(conta1.saldo)
conta1.adicionarJuros()
print(conta1.saldo)
conta1.adicionarJuros()
print(conta1.saldo)
