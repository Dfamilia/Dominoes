####################################
######### Librerias ################
####################################

from Jugador import Jugador
from Ficha import Ficha

import sys
from Funciones import *
from random import choice
from random import shuffle

####################################
######### Clases ###################
####################################

class Mesa(Ficha, Jugador):

    def __init__(self, modoJuego = "1vs3", jugarHasta = 500):
        self.__jugadores = []
        self.__fichasEnMesa = None
        self.__modoJuego = modoJuego
        self.__jugarHasta = jugarHasta

    ####################################
    ######### SETTERS ##################
    ####################################

    #METODO: crea e inicializa las 28 fichas del domino en la mesa para que se pueda jugar
    @property
    def __iniciarDominoes(self):
        a, b, totalFichas, fichas, self.__fichasEnMesa= 0, 0, 0, [], []

        while totalFichas < 28:
            fichas.append(Ficha(a,b))            
            if a == b:
                a += 1
                b = 0
            else:
                b += 1
            totalFichas += 1
        self.__fichasEnMesa = fichas

    #METODO: registra los jugadores
    def registrarJugadores(self, jugadores):

        for jugador,status in jugadores:
            self.__jugadores.append(Jugador(jugador, status))
            # print(jugadores[jugador], jugadores[status])
        
    #METODO: agrega la ficha desde el jugador a la mesa por el terminal derecho
    def __agregarPorDer(self, ficha):
        self.__fichasEnMesa.append(ficha)

    #METODO: agrega la ficha desde el jugador a la mesa por el terminal izquierdo
    def __agregarPorIzq(self, ficha):
        self.__fichasEnMesa.insert(0, ficha)

    ####################################
    ######### GETTERS ##################
    ####################################

    #METODO: retorna las fichas que estan en la mesa
    @property
    def __getDominosEnMesa(self):
        return self.__fichasEnMesa
    
    #METODO: retorna el array de jugadores que podran jugar
    @property
    def __getJugadores(self):
        return self.__jugadores
    
    #METODO: retorna el modo de juego
    @property
    def __getModo(self):
        return self.__modoJuego
    
    #METODO: retorna hasta cuantos puntos debe continuar el juego
    @property
    def __getjugarHasta(self):
        return self.__jugarHasta
        
    #METODO: revolver las fichas
    @property
    def __revolverFichas(self):
        shuffle(self.__getDominosEnMesa)

    #METODO: reparte las fichas entre los jugadores
    @property
    def __repartirFichas(self):
        
        for jugador in self.__jugadores:
            while jugador._getTotalFichasJugador < 7:
                jugador._setFichas(self.__fichasEnMesa.pop())
    
    #METODO: muestra las fichas jugadas en la mesa de juego
    def __mostrarMesa(self):

        mesa = "Mesa de juego: "
        for ficha in self.__getDominosEnMesa:
            mesa += "{}".format(str(ficha))
        return mesa

    #METODO: ingresa los puntos ganados por los jugadores en cada jugadas y retorna resultados
    def __resultadosPorPartida(self, jugadorActual, ganoPor):

        if ganoPor == "DOMINACION" or ganoPor == "CAPICUA":
            totalpuntos = 0
            
            for jugador in self.__getJugadores:
                totalpuntos += jugador._getTotalPuntosJugador
            
                if ganoPor == "CAPICUA":
                    totalpuntos += 25

            jugadorActual._setPuntosGanados(totalpuntos)
            return jugadorActual, "{}, Gana por: {}! la partida.. Gana: {} puntos".format(jugadorActual._getNombreJugador, ganoPor, totalpuntos)

        elif ganoPor == "TRANQUE":
            jugadorGanador = jugadorActual
            tabla1 = ""
            tabla2 = ""
            totalpuntos = 0
            
            for jugador in self.__getJugadores:
                tabla1 += " {} tiene: {} puntos; ".format(jugador._getNombreJugador, jugador._getTotalPuntosJugador)
                totalpuntos += jugador._getTotalPuntosJugador
                
                if jugador._getTotalPuntosJugador < jugadorGanador._getTotalPuntosJugador:
                    jugadorGanador = jugador
            
            jugadorGanador._setPuntosGanados(totalpuntos)
            tabla2 = "{} Tranca el juego; {} Gana la partida por menos puntos; Gana: {} puntos".format(jugadorActual._getNombreJugador,jugadorGanador._getNombreJugador, totalpuntos)
            return jugadorGanador, tabla1, tabla2
    
    def __mostrarTablaDeResultados(self):
        pass

    #METODO: ejecuta el juego
    def jugarDomino(self):

        #inicializo los dominos en la mesa
        self.__iniciarDominoes
        #guarda el jugador que realizo la jugada ganadora
        Ganador = ""

        #Jugar hasta llegar al puntaje propuesto por __jugarHasta
        while self.__getJugadores[0]._getPuntosGanadosJugador < self.__jugarHasta and self.__getJugadores[1]._getPuntosGanadosJugador < self.__jugarHasta and self.__getJugadores[2]._getPuntosGanadosJugador < self.__jugarHasta and self.__getJugadores[3]._getPuntosGanadosJugador < self.__jugarHasta:

            #revuelvo las fichas
            self.__revolverFichas
            #reparto las fichas entre los jugadores
            self.__repartirFichas            
            #lleva un conteo de pases para saber cuando el juego esta trancado
            passCont = 0
            #variable jInicial
            jugadaInicial = False
            #pLateral obtiene el valor del terminal izquierdo y derecho de la mesa que se puede hacer jugada
            pLateral,uLateral = None,None
            #lleva un registro de las jugadas total realizadas/ registro de jugadas por ronda
            registroTotal, registroRonda = [],[]
            
            #La partida se ejecutara mientras que 1 jugador posea fichas o el juego este tranchado
            Partida = True
            while Partida:

                #limpiador de consola
                # cls()

                #Si es la jugada inicial se ejecutara este script
                if len(self.__getDominosEnMesa) == 0:
                    jugadaInicial = True
                    
                    #se toma el ganador de la primera partida en adelante
                    if Ganador:
                        jugadorActual = Ganador
                        posJugadorActual = self.__getJugadores.index(jugadorActual)
                        
                    else:
                        #obtengo un jugador aleatorio para la jugada inicial
                        jugadorActual = choice(self.__getJugadores)
                        #obtengo la posicion del jugador inicial para poder seguir con los otros jugadores
                        posJugadorActual = self.__getJugadores.index(jugadorActual)      
                
                #jugador automatico
                if jugadorActual._getStatusJugador == "CPU":
                    #recibo la posicion de la jugada y la ficha del metodo Jugar del Jugador CPU
                    posJugada, fichaActual = jugadorActual._jugarCPU(pLateral, uLateral, jugadaInicial)
                
                #jugador humano
                elif jugadorActual._getStatusJugador == "HM":
                    cls()
                    header()

                    #recibo la posicion de la jugada y la ficha del metodo Jugar del Jugador HM
                    #muestra la mesa y las jugadas realizadas por otros jugadores antes que yo jugar
                    print('\n\n ',self.__mostrarMesa(),'\n\n  Historial de Ronda: \n')
                    for e in registroRonda:
                        if not "HM" in e:
                            print(" ",e)
                        
                    posJugada, fichaActual = jugadorActual._jugarHM(pLateral, uLateral, jugadaInicial)
                    #elimino la ronda visualisada
                    registroRonda = []

                #determina que el jugador no posee fichas jugables y pasa
                if not posJugada:
                    #actualizo el contador de pases
                    passCont += 1
                
                #determina que el jugador jugara por el terminal derecho
                if (posJugada == "terminalDerecho"):             
                    #realizo la jugada
                    self.__agregarPorDer(fichaActual)
                    #mantengo el nombre del jugador que realizo la ultima jugada
                    Ganador = jugadorActual
                
                #determina que el jugador jugara por el terminal izquierdo
                if (posJugada == "terminalIzquierdo"):
                    self.__agregarPorIzq(fichaActual)
                    Ganador = jugadorActual
                
                #registro la jugada realizada
                registroRonda.append("{0:3}: {1:6} JUGO: {2}".format(jugadorActual._getStatusJugador,jugadorActual._getNombreJugador, fichaActual))
                
                ### front ###
                cls()
                header()
                print('\n\n ',self.__mostrarMesa(),'\n')
                input(f"  {jugadorActual._getNombreJugador} jugo: {fichaActual}")
                        
                #si el jugador hizo una jugada se elimina la ficha del jugador
                if posJugada:
                    if passCont == 3:
                        if (jugadorActual._getPuntosGanadosJugador + 25) < self.__getjugarHasta:
                            jugadorActual._setPuntosGanados(25)
                            print("{} consigue 25 por pases!!!".format(jugadorActual._getNombreJugador))
                            input()
                            registroRonda.append("Jugador: {} consigue 25 por pases!!!".format(Ganador._getNombreJugador))
                        else:
                            print("{} no le caben los 25!!!".format(jugadorActual._getNombreJugador))
                            input()


                    #reseteo el contador de pases
                    passCont = 0
                    #remueve la ficha jugada del jugador
                    jugadorActual._delFichaJugada(fichaActual)
            

                if jugadorActual._getTotalFichasJugador != 0 and passCont != 4:
                    #se realizo la primera jugada
                    jugadaInicial = False

                    #actualizo el valor de los terminales de la mesa de jugo despues de cada jugada
                    pLateral = self.__getDominosEnMesa[0]._getLadoA
                    uLateral = self.__getDominosEnMesa[len(self.__getDominosEnMesa)-1]._getLadoB

                    #actualizo la posicion del jugador actual despues de cada ronda
                    if posJugadorActual == 3:
                        posJugadorActual = -1

                        #concateno el registroRonda al registroTotal
                        registroTotal += registroRonda                   

                    #actualizo la posicion del jugador actual para pasar al siguiente jugador
                    posJugadorActual += 1
                    jugadorActual = self.__getJugadores[posJugadorActual]

                else:
                    
                    #formas de ganar
                    if jugadorActual._getTotalFichasJugador == 0:
                        if pLateral != uLateral and (fichaActual._getLadoA == pLateral and fichaActual._getLadoB == uLateral) or (fichaActual._getLadoA == uLateral and fichaActual._getLadoB == pLateral):
                            Ganador, resultado = self.__resultadosPorPartida(jugadorActual,"CAPICUA")
                            registroRonda.append(resultado)

                        else:
                            Ganador, resultado = self.__resultadosPorPartida(jugadorActual,"DOMINACION")
                            registroRonda.append(resultado)
                    
                    if passCont == 4:
                        Ganador, tabla1, tabla2 = self.__resultadosPorPartida(jugadorActual,"TRANQUE")
                        registroRonda.append(tabla1)
                        registroRonda.append(tabla2)

                    #TERMINO EL JUEGO
                    Partida = False
                    #concateno el registroRonda al registroTotal
                    registroTotal += registroRonda
 
                    print("\n\n")
                    for e in registroTotal:
                        print("  ",e)

                    for jugador in self.__getJugadores:
                        self.__fichasEnMesa += jugador._devolverFichasDelJugador()

                    input("\n\n  FIN de partida, Devolviendo las fichas sobrantes de los jugadores a la mesa, presiona cualquier tecla para seguir jugando....")

            
###############################################
########### Pruebas ###########################
###############################################

#jugadores
pedro = Jugador("Pedro",'HM')
juan = Jugador("Juan")
manuel = Jugador("Manuel")
vale = Jugador("Vale")

#mesa
mesa = Mesa()
# mesa.
# print(mesa._getDominosEnMesa)
# for e in mesa._getDominosEnMesa:
#     e.girar()
#     print(e)

# mesa.


# print(mesa.getPrueba())


jugadores = [["darlin","HM"],["pedro", "CPU"],["jose", "CPU"],["alejandro", "CPU"]]
mesa.registrarJugadores(jugadores)

print("estamos en la mesa de jugo")
mesa.jugarDomino()

### IDEAS ### 
#AminMoya001
#829-645-2685


#si se juega de 2, poner una variable como reserva de las fichas restante y adicionarle el revolver simulando cojida de ficha aleatoria, ya que se utilizara el pop() para obtenerla

##Dante

##dividir el proyecto por archivos, menu, gameLoope, resultados
##hacer que el usuario juegue, 1, 2 jugadores
##si es posible hacerlo grafico