####################################
######### Librerias ################
####################################

#os te permite interactuar con la consola
import os
#importando la clase ficha
from Ficha import *

####################################
######### Funciones ################
####################################

#funcion que limpia la pantalla de la consola
def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#funcion que crea las fichas del domino
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

#funcion que reparte las fichas a los jugadores
def repartidor(jugador, listaDominoes):
    if jugador.totalFichas == 7:
        return jugador
    else:
        jugador.fichas.append(listaDominoes.pop())
        jugador.totalFichas += 1
        return repartidor(jugador, listaDominoes)

#funcion que retorna el jugador con menos puntos en sus fichas despues de un tranque
def jugadorPuntos(jugador):

    totalPuntos = 0
    for ficha in jugador.fichas:
        totalPuntos += (ficha.ladoA + ficha.ladoB)
    return totalPuntos