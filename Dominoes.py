####JUEGO DOMINOES####
#crear estructura para una ficha !
#funcion girar ficha !
#crear todas las fichas !
#crear estructura para la mesa o tablero de juego
#revolver las fichas
#crear estructura para un jugador
#jugar con 4 jugadores

#estructura para la ficha
class Ficha:
    def __init__(self, a, b):
        self.ladoA = a
        self.ladoB = b
        self.ficha = [self.ladoA, self.ladoB]
    
    def girar(self):

        self.ladoA, self.ladoB = self.ladoB, self.ladoA
        
        self.ficha = [self.ladoA, self.ladoB]
    
    def __str__(self):
        return "{}".format(self.ficha)

        
#crea la estructura para guargar dominoes
#se comenta para probar que no se necesita para
#crear los dominoes
# class Dominoes:

#     def __init__(self):
#         self.dominoes = []

#     def add_dominoes(self, ficha):
#         self.dominoes.append(ficha)

#     def getDominoes(self):
#         return self.dominoes
    
#     def __str__(self):
#         stringResult = ""
#         for e in self.dominoes:
#             stringResult += "{} \n".format(e.ficha)
#         return stringResult


#crea las 28 fichas del domino
def crearDominoes(Dominoes = [], ladoA = 0, ladoB = 0, cont = 0):

    if cont == 28:
        return Dominoes
    else:
        # Dominoes.add_dominoes(Ficha(ladoA,ladoB))
        Dominoes.append(Ficha(ladoA,ladoB))
        
        if ladoA == ladoB:
            return crearDominoes(Dominoes, ladoA+1, 0, cont+1)
        else:
            return crearDominoes(Dominoes, ladoA, ladoB+1, cont+1)


# dominoes = Dominoes()
print(crearDominoes())
print()

for e in crearDominoes():
    print(str(e))

# ficha = dominoes.getDominoes()[4]
# print(ficha)
# ficha.girar()
# print(ficha)
