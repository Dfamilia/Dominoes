####JUEGO DOMINOES####
#crear estructura para una ficha !
#funcion girar ficha !
#crear todas las fichas !
#crear estructura para la mesa o tablero de juego
#revolver las fichas
#crear estructura para un jugador
#jugar con 4 jugadores

####################################
######### Librerias ################
####################################

import random

####################################
######### Funciones ################
####################################

def Dominoes(allFichas = [], ladoA = 0, ladoB = 0, cont = 0):
    
    #CONSTANTE para la cantidad de fichas
    TOTALFICHAS = 28

    if cont == TOTALFICHAS:
        return allFichas
    else:
        
        #agrega las fichas al array
        allFichas.append(Ficha(ladoA, ladoB))
        
        if ladoA == ladoB:
            return Dominoes(allFichas, ladoA+1, 0, cont+1)
        else:
            return Dominoes(allFichas, ladoA, ladoB+1, cont+1)

####################################
######### Clases ###################
####################################

#estructura para la ficha
class Ficha:
    def __init__(self, a, b):
        self.ladoA = a
        self.ladoB = b
        self.ficha = [self.ladoA, self.ladoB]
    
    #metodo para girar la ficha
    def girar(self):

        #se realizo para que sea mas entendible el cambio
        self.ladoA, self.ladoB = self.ladoB, self.ladoA
        #se asignan nuevos valores a la lista
        self.ficha = [self.ladoA, self.ladoB]
    
    #imprimir la ficha
    def __str__(self):
        return "{}".format(self.ficha)

#TODO crear estructura para jugador
#TODO el jugador verifica que puede jugar, si es asi juega la ficha
class Jugador:

    def __init__(self, nomJugador):
        self.nombre = nomJugador
        self.fichas = []
        self.totalFichas = 0

    #se llama este metodo si el jugador necesita una ficha aparte de las que reparte la mesa
    def addFicha(self, ficha):
        self.fichas = ficha
        self.totalFichas += 1

#creando la estructura de la mesa de juego
#DONE la mesa revuelve las fichas
#TODO la mesa reparte las fichas
#TODO la mesa asigna el turno al jugador
#TODO la mesa mantiene un registro de fichas jugadas
#TODO la mesa tiene un metodo jugar donde se desarrolla todo el juego de domino y sera el metodo que se llamara para ejecutar el juego 
#DONE la mesa mantiene un registro de el primer valor de ficha jugada y el ultimo valor de ficha jugada [A|B][B|C][C|D] => V1 = A, V2 = D, esto para saber en que posicion podemos jugar la nueva ficha 

#USAR la clase ficha por herencia
#USAR la clase jugador por composicion
class Mesa(Ficha):

    #guardando todas las fichas en una variable de clase para que pueda ser accedida su informacion desde todos los objetos 
    #fichas = crearDominoes()
    
    def __init__(self, pFicha = None, uFicha = None):
        # self.pFicha = pFicha
        # self.uFicha = uFicha
        # self.totalFichas = 0
       # print(Dominoes())
        self.dominoes = Dominoes()
        
    def getDominoes(self):
        return self.dominoes

    #metodo para revolver las fichas
    def revolverFichas(self):
        random.shuffle(self.dominoes)

    #metodo que ejecuta el juego
    def playDomino(self):
        pass




###############################################
########### Pruebas ###########################
###############################################

mesa = Mesa()
#print(mesa.getDominoes())
for e in mesa.getDominoes():
    print(e)
print()
print("revuelvo las fichas")
mesa.revolverFichas()
print()
for e in mesa.getDominoes():
    print(e)
#print(mesa.revolverFichas())