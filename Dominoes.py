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

# e4from Ficha import *
from Jugador import *
from Funciones import *

####################################
######### Funciones ################
####################################

#funcion que crea las fichas del domino
# def Dominoes(allFichas = [], ladoA = 0, ladoB = 0, cont = 0):
    
#     #CONSTANTE para la cantidad de fichas
#     TOTALFICHAS = 28

#     if cont == TOTALFICHAS:
#         return allFichas
#     else:
#         #agrega las fichas al array
#         allFichas.append(Ficha(ladoA, ladoB))
        
#         if ladoA == ladoB:
#             return Dominoes(allFichas, ladoA+1, 0, cont+1)
#         else:
#             return Dominoes(allFichas, ladoA, ladoB+1, cont+1)

# #funcion que reparte las fichas a los jugadores
# def repartidor(jugador, listaDominoes):
#     if jugador.totalFichas == 7:
#         return jugador
#     else:
#         jugador.fichas.append(listaDominoes.pop())
#         jugador.totalFichas += 1
#         return repartidor(jugador, listaDominoes)

# #funcion que retorna el jugador con menos puntos en sus fichas despues de un tranque
# def jugadorPuntos(jugador):

#     totalPuntos = 0
#     for ficha in jugador.fichas:
#         totalPuntos += (ficha.ladoA + ficha.ladoB)
#     return totalPuntos

####################################
######### Clases ###################
####################################

class Mesa(Ficha):
    
    def __init__(self, *jugadores):
        
        #array jugadores
        self.jugadores =  jugadores
        self.dominoesEnMesa = Dominoes()
        
    #metodo para revolver las fichas
    def revolverFichas(self):
        random.shuffle(self.dominoesEnMesa)

    #metodo que reparte las fichas entre los jugadores
    def repartirFichas(self):
        
        for jugador in self.jugadores:  

            #funcion que reparte fichas a un jugador determinado   
            repartidor(jugador, self.dominoesEnMesa)
    
    #metodo que muestra las fichas jugadas en la mesa de juego
    def mostrarMesa(self):

        mesa = "Mesa de juego: "
        for ficha in self.dominoesEnMesa:
            mesa += "{}".format(str(ficha))
        return mesa

    #metodo que ejecuta el juego
    def playDomino(self):
        
        #revuelvo las fichas
        self.revolverFichas()
        #reparto las fichas entre los jugadores
        self.repartirFichas()
        
        #guarda el jugador que realizo la jugada ganadora
        Ganador = ""
        #lo utilizo para saber cual jugador juega
        posJugadorActual = 0
        #pLateral obtiene el valor del terminal izquierdo de la mesa que se puede hacer jugada
        pLateral = None
        #uLateral obtiene el valor del terminal derecho de la mesa que se puede hacer jugada
        uLateral = None
        #lleva un conteo de pases para saber cuando el juego esta trancado
        passCont = 0
        #lleva un registro de las jugadas realizadas
        registro =[]
        
        #registro de jugadores, jugadas y sus fichas
        registro.append("****************************** Fichas de los jugadores ******************************")
        registro.append("")
        
        for jugador in self.jugadores:
            registro.append("{}--:{}".format(jugador.nombre,jugador.fichasDelJugador()))
        
        registro.append("")
        registro.append("********************************* Empieza el juego *********************************")
        registro.append("")

        #obtengo un jugador aleatorio para la jugada inicial
        jugadorActual = random.choice(self.jugadores)
        #obtengo la posicion del jugador inicial para poder seguir con los otros jugadores
        posJugadorActual = self.jugadores.index(jugadorActual)

        #sera True hasta que 1 jugador se quede sin fichas o el juego este tranchado
        partida = True
        while partida:
            #recibo la posicion de la jugada y la ficha del metodo Jugar del Jugador
            posJugada, fichaActual = jugadorActual.Jugar(self.dominoesEnMesa, pLateral, uLateral)

            #determina que el jugador no posee fichas jugables y pasa
            if not posJugada:
                #actualizo el contador de pases
                passCont += 1
            
            #determina que el jugador jugara por el terminal derecho
            if (posJugada == "uLateral"):
                
                #reseteo el contador de pases
                passCont = 0
                #realizo la jugada
                self.dominoesEnMesa.append(fichaActual)
                #mantengo el nombre del jugador que realizo la ultima jugada
                Ganador = jugadorActual
            
            #determina que el jugador jugara por el terminal izquierdo
            if (posJugada == "pLateral"):
                
                passCont = 0
                self.dominoesEnMesa.insert(0, fichaActual)
                Ganador = jugadorActual
            
            #registro la jugada realizada
            registro.append("JUGADOR: {} FICHAS: {}".format(jugadorActual.nombre, jugadorActual.fichasDelJugador())) 
            registro.append("JUGADOR: {} JUGO: {}".format(jugadorActual.nombre, fichaActual))
            registro.append("")
            
            #VISTA DETALLADA/ COMENTAR PARA UUSAR LA VISTA SIMPLE
            # registro.append("")
            # registro.append(self.mostrarMesa())
            # registro.append("")

            #si el jugador hizo una jugada se elimina la ficha del jugador
            if posJugada:
                #remueve la ficha jugada del jugador
                jugadorActual.fichas.remove(fichaActual)
                jugadorActual.totalFichas -= 1
         

            if jugadorActual.totalFichas != 0 and passCont != 4:

                #actualizo el valor de los terminales de la mesa de jugo despues de cada jugada
                pLateral = self.dominoesEnMesa[0].ladoA
                uLateral = self.dominoesEnMesa[len(self.dominoesEnMesa)-1].ladoB

                #actualizo la posicion del jugador actual despues de cada ronda
                if posJugadorActual == 3:
                    posJugadorActual = -1

                #actualizo la posicion del jugador actual para pasar al siguiente jugador
                posJugadorActual += 1
                jugadorActual = self.jugadores[posJugadorActual]

            else:

                #partida termino
                partida = False
                
                #formas de ganar
                if jugadorActual.totalFichas == 0:

                    if (fichaActual.ladoA == pLateral and fichaActual.ladoB == uLateral) or (fichaActual.ladoA == uLateral and fichaActual.ladoB == pLateral) and pLateral != uLateral:
                        registro.append("Jugador: {} Domina con KAPICUA!!!".format(Ganador.nombre))
                    else:
                        registro.append("Jugador: {} Domina!!!".format(Ganador.nombre))
                
                if passCont == 4:
                    for jugador in self.jugadores:
                        if jugadorPuntos(Ganador) > jugadorPuntos(jugador):
                            Ganador = jugador

                    #menosPuntos(self.jugadores[0],self.jugadores[1],self.jugadores[2],self.jugadores[3])
                    registro.append("Jugador: {} Gana por puntos, Juego Trancado !!!".format(Ganador.nombre))
                    

        #muestro la mesa de juego y el registro de las jugadas/ VISTA SIMPLE
        
        print()
        for e in registro:
            print(e)
        
        print()
        print(self.mostrarMesa())

            
###############################################
########### Pruebas ###########################
###############################################

#jugadores
pedro = Jugador("Pedro")
juan = Jugador("Juan")
manuel = Jugador("Manuel")
vale = Jugador("Vale")

#mesa
mesa = Mesa(pedro, juan, manuel, vale)

print("Prueba de suma de puntos")
mesa.revolverFichas()
mesa.repartirFichas()

#print(jugadorPuntos(pedro))

print("estamos en la mesa de jugo")
mesa.playDomino()

### IDEAS ### 
#AminMoya001
#829-645-2685


#si se juega de 2, poner una variable como reserva de las fichas restante y adicionarle el revolver simulando cojida de ficha aleatoria, ya que se utilizara el pop() para obtenerla

##Dante

##dividir el proyecto por archivos, menu, gameLoope, resultados
##hacer que el usuario juegue, 1, 2 jugadores
##si es posible hacerlo grafico