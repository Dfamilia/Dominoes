#archivo que crea las fichas del juego
class Ficha:
    def __init__(self, a, b):
        self.ladoA = a
        self.ladoB = b
        self.ficha = [self.ladoA, self.ladoB]
    
    def girar(self):

        self.ladoA, self.ladoB = self.ladoB, self.ladoA
        
        self.ficha = [self.ladoA, self.ladoB]
        

class Dominoes:

    def __init__(self):
        self.dominoes = []

    def add_dominoes(self, ficha):
        self.dominoes.append(ficha)
    
    def __str__(self):
        stringResult = ""
        for e in self.dominoes:
            stringResult += "{} \n".format(e.ficha)
        return stringResult

def crearDominoes(Dominoes, ladoA = 0, ladoB = 0, cont = 0):

    if cont == 28:
        return Dominoes
    else:
        Dominoes.add_dominoes(Ficha(ladoA,ladoB))
        
        if ladoA == ladoB:
            return crearDominoes(Dominoes, ladoA+1, 0, cont+1)
        else:
            return crearDominoes(Dominoes, ladoA, ladoB+1, cont+1)


dominoes = Dominoes()
print(crearDominoes(dominoes))
#print(dominoes)
        
    