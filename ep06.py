class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def aumentarSalario(self, porcentagem):
        aumento_porcentagem = 1 + (porcentagem / 100)
        self.salario *= aumento_porcentagem
        return f"{self.salario:.2f}"

funcionario1 = Funcionario("Ednaldo", 2500)
funcionario2 = Funcionario("Pedro", 1500)
print(funcionario1.aumentarSalario(20))
print(funcionario2.aumentarSalario(50))
