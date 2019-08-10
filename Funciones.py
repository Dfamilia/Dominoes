####################################
######### Librerias ################
####################################

#os te permite interactuar con la consola
import os

####################################
######### Funciones ################
####################################

#funcion que limpia la pantalla de la consola
def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#funcion que retorna el jugador con menos puntos en sus fichas despues de un tranque
def jugadorPuntos(jugador):

    totalPuntos = 0
    for ficha in jugador.fichas:
        totalPuntos += (ficha._getLadoA + ficha._getLadoB)
    return totalPuntos