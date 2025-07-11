class Lista:
    def __init__(self, itens):
        self.itens = itens
    
    def listaSemRepeticao(self):
        self.listaSemRepeticao = list(set(self.itens))
        print(*self.listaSemRepeticao)

lista1 = Lista([1,1,2,2,3,5,5,6])
lista1.listaSemRepeticao()
