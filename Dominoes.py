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

    def __init__(self):
        self.__fichasEnMesa = None
        self.__jugadores = []
        self.__modoJuego = None
        self.__jugarHasta = None

    ####################################
    ######### SETTERS ##################
    ####################################

    #METODO: registra los jugadores
    def _setRegistrarJugadores(self, jugadores):

        for jugador,status in jugadores:
            self.__jugadores.append(Jugador(jugador, status))
            # print(jugadores[jugador], jugadores[status])
    
    #METODO: establece el modo de juego    
    def _setModoJuego(self, modoJuego):
        self.__modoJuego = modoJuego

    #METODO: indica hasta cuantos puntos se desarrollara el juego    
    def _setJugarHasta(self, jugarHasta):
        self.__jugarHasta = jugarHasta        
        
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

    ####################################
    ######### METODOS ##################
    ####################################
        
    #METODO: crea e inicializa las 28 fichas del domino en la mesa para que se pueda jugar
    @property
    def __crearDominoes(self):
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
    
    #METODO: agrega la ficha desde el jugador a la mesa por el terminal derecho
    def __agregarPorDer(self, ficha):
        self.__fichasEnMesa.append(ficha)

    #METODO: agrega la ficha desde el jugador a la mesa por el terminal izquierdo
    def __agregarPorIzq(self, ficha):
        self.__fichasEnMesa.insert(0, ficha)
    
    #METODO: retorna el jugador inicial de cada partida
    def __jugadorInicial(self, ganador = None):
        #se toma el ganador de la primera partida en adelante
        if ganador:
            posJugadorActual = self.__getJugadores.index(ganador)
            return ganador, posJugadorActual
            
        else:
            #obtengo un jugador aleatorio para la jugada inicial
            jugadorActual = choice(self.__getJugadores)
            #obtengo la posicion del jugador inicial para poder seguir con los otros jugadores
            posJugadorActual = self.__getJugadores.index(jugadorActual)  
            return jugadorActual, posJugadorActual
    
    #METODO: se ejecuta cuando es el turno del jugadorCPU
    def __turnoJugadorCPU(self, pLateral, uLateral, jugadaInicial, jugadorActual):
        
        #recibo la posicion de la jugada y la ficha del metodo Jugar del Jugador CPU
        posJugada, fichaActual = jugadorActual._jugarCPU(pLateral, uLateral, jugadaInicial)

        if self.__getModo == "CPUvsCPU":
            # ### front ###
            cls()
            self.__mostrarTablaResultados
            print('\n\n ',self.__mostrarMesa(),'\n')
            input(f"  {jugadorActual._getNombreJugador} jugo: {fichaActual}")
       
        return posJugada, fichaActual

    #METODO: se ejecuta cuando es el turno del jugador humano
    def __turnoJugadorHM(self, registroRonda, pLateral, uLateral, jugadaInicial, jugadorActual):

        #limpio la pantalla y muestro el banner
        cls()
        self.__mostrarTablaResultados

        #recibo la posicion de la jugada y la ficha del metodo Jugar del Jugador HM
        #muestra la mesa y las jugadas realizadas por otros jugadores antes que yo jugar
        print('\n\n ',self.__mostrarMesa(),'\n')

        #observo las jugadas de los demas jugadores previos
        hr("\n")        
        for e in registroRonda:
            if not "HM" in e:
                print(" ",e)
        hr("")        
        
        return jugadorActual._jugarHM(pLateral, uLateral, jugadaInicial)

    #METODO: ejecuta la jugada que hace el jugador
    def __jugadaDelJugadorEnMesa(self, posJugada, fichaActual):

        #determina que el jugador jugara por el terminal derecho
        if (posJugada == "terminalDerecho"):             
            #realizo la jugada
            self.__agregarPorDer(fichaActual)
        
        #determina que el jugador jugara por el terminal izquierdo
        if (posJugada == "terminalIzquierdo"):
            self.__agregarPorIzq(fichaActual)
            
    #METODO: establece los puntos ganados por el jugador al pasar a todos los jugadores restantes de la mesa de forma consecutiva
    def __puntosGanadosPorPases(self, jugadorActual, registroRonda):

        if (jugadorActual._getPuntosGanadosJugador + 25) < self.__getjugarHasta:
            jugadorActual._setPuntosGanados(25)
            print("\n\n  {} consigue 25 por pases!!!".format(jugadorActual._getNombreJugador))
            input()
            registroRonda.append("Jugador: {} consigue 25 por pases!!!".format(jugadorActual._getNombreJugador))
        else:
            print("\n\n  {} no le caben los 25!!!".format(jugadorActual._getNombreJugador))
            input()

    #METODO: muestra las fichas jugadas en la mesa de juego
    def __mostrarMesa(self):

        mesa = "|||-->MESA<--|||::> "
        for ficha in self.__getDominosEnMesa:
            mesa += "{}".format(str(ficha))
        mesa += " <::|||"
        return mesa

    #METODO: determina la forma en la que gana un jugador, ingresa los puntos ganados por los jugadores en cada jugadas y retorna resultados
    def __modosDeGanarPartida(self, jugadorActual, ganoPor):

        #se ejecuta este script si el jugador se le acaban las fichas
        if ganoPor == "DOMINACION" or ganoPor == "CAPICUA":
            totalpuntos = 0
            
            for jugador in self.__getJugadores:
                totalpuntos += jugador._getTotalPuntosJugador
            
            if ganoPor == "CAPICUA":
                ganoPor += " + 25"
                totalpuntos += 25

            jugadorActual._setPuntosGanados(totalpuntos)
            return jugadorActual, "\n  {}, Gana por: {}! la partida.. Gana: {} puntos".format(jugadorActual._getNombreJugador, ganoPor, totalpuntos)

        #se ejecuta este script si se tranco el juego
        elif ganoPor == "TRANQUE":
            jugadorGanador = jugadorActual
            tablaJugadorPuntos, totalpuntos = "\n", 0
            
            for jugador in self.__getJugadores:
                tablaJugadorPuntos += "  {} tiene: {} puntos; ".format(jugador._getNombreJugador, jugador._getTotalPuntosJugador)
                totalpuntos += jugador._getTotalPuntosJugador
                
                if jugador._getTotalPuntosJugador < jugadorGanador._getTotalPuntosJugador:
                    jugadorGanador = jugador
            
            jugadorGanador._setPuntosGanados(totalpuntos)
            tablaJugadorPuntos += "\n  {} Tranca el juego; {} Gana la partida por menos puntos; Gana: {} puntos".format(jugadorActual._getNombreJugador,jugadorGanador._getNombreJugador, totalpuntos)

            return jugadorGanador, tablaJugadorPuntos
    
    #METODO: agrega el tipo de fin de jugada al registro y devuelve el registro
    def __finDePartida(self, Ganador, fichaGanadora, terminalIzq, terminalDer, passCont, registroPartidas):

        if Ganador._getTotalFichasJugador == 0:
            if (terminalIzq != terminalDer) and ((fichaGanadora._getLadoA == terminalIzq and fichaGanadora._getLadoB == terminalDer) or (fichaGanadora._getLadoA == terminalDer and fichaGanadora._getLadoB == terminalIzq)):
                Ganador, resultado = self.__modosDeGanarPartida(Ganador,"CAPICUA")
                registroPartidas.append(resultado)

            else:
                Ganador, resultado = self.__modosDeGanarPartida(Ganador,"DOMINACION")
                registroPartidas.append(resultado)
            
        if passCont == 4:
            Ganador, tablaJugadorPuntos = self.__modosDeGanarPartida(Ganador,"TRANQUE")
            registroPartidas.append(tablaJugadorPuntos)
        
        return registroPartidas

    #METODO: muestra el logo de DOMINOES y los puntos ganados por los jugadores
    @property
    def __mostrarTablaResultados(self):
        #cabecera del proyecto
        banner()

        hr("\n")
        tabla = " *******"
        for jugador in self.__getJugadores:
            tabla += f"| {jugador._getStatusJugador}: {jugador._getNombreJugador}: [{jugador._getPuntosGanadosJugador}] |**************************"
        
        print(tabla)
        hr("")

    #METODO: muestra la tabla de resultado final de una partida
    def __tablaDeFinDePartida(self, registroPartidas):

        #limpio la pantalla y muestro el banner
        cls()
        self.__mostrarTablaResultados

        #recibo la posicion de la jugada y la ficha del metodo Jugar del Jugador HM
        #muestra la mesa y las jugadas realizadas por otros jugadores antes que yo jugar
        print('\n\n ',self.__mostrarMesa(),'\n')
        
        #muestro el registro de jugadas
        print("\n")
        for e in registroPartidas:
            print("  ",e)
        
        #devuelvo las fichas que no fueron jugadas por cada jugador
        for jugador in self.__getJugadores:
            self.__fichasEnMesa += jugador._devolverFichasDelJugador

    #METODO: ejecuta las jugadas necesarias para que termine una partida de domino y devuelve un resultado
    def __ciclosDePartida(self, Ganador):
        
        #cicloPartida = sera verdadera hasta que un jugador gane la partida por DOMINACION, CAPICUA O TRANQUE
        #passCont = lleva un conteo de pases para saber cuando el juego esta trancado
        #pLateral/uLateral = obtienen el valor del terminal izquierdo y derecho de la primera y ultima ficha de la mesa que se puede hacer jugada
        #registroTotal = lleva un registro de todas las jugadas realizadas
        #registroRonda = lleva un registro de todas las jugadas realizadas en cada ronda
        jugadaInicial, passCont, terminalIzq, terminalDer, registroPartidas, registroRonda  = True, 0, None, None, [], []

        #establesco el jugador inicial/ si es una segunda partida inicia el ganador de la anterior
        jugadorActual, posJugadorActual = self.__jugadorInicial(Ganador)
        while jugadorActual._getTotalFichasJugador != 0 and passCont != 4:

            #jugador automatico
            if jugadorActual._getStatusJugador == "CPU":
                posJugada, fichaActual = self.__turnoJugadorCPU(terminalIzq, terminalDer, jugadaInicial, jugadorActual)                   
            
            #jugador humano
            elif jugadorActual._getStatusJugador == "HM":
                posJugada, fichaActual = self.__turnoJugadorHM(registroRonda, terminalIzq, terminalDer, jugadaInicial, jugadorActual)

                #elimino la ronda visualisada
                registroRonda = []

            #determina si el jugador realizo una jugada o realizo un pase
            if posJugada:
                self.__jugadaDelJugadorEnMesa(posJugada, fichaActual)
                Ganador, fichaGanadora = jugadorActual, fichaActual

                #si el jugador pasa al resto de jugadores en su proximo turno obtiene 25 puntos por pases                    
                if passCont == 3:
                    self.__puntosGanadosPorPases(jugadorActual, registroRonda)
            
                #reseteo el contador de pases
                passCont = 0
            else:
                #actualizo el contador de pases
                passCont += 1                    

            #registro la jugada realizada
            registroRonda.append("{0:3}: {1:6} JUGO: {2}".format(jugadorActual._getStatusJugador,jugadorActual._getNombreJugador, fichaActual))

            #actualizo la posicion del jugador actual despues de cada ronda
            if posJugadorActual == 3 or jugadorActual._getTotalFichasJugador == 0 or passCont == 4:
                posJugadorActual = -1

                #concateno el registroRonda al registroTotal
                registroPartidas += registroRonda  

            if Ganador._getTotalFichasJugador != 0 and passCont != 4:
                
                #actualizo el valor de los terminales de la mesa de jugo despues de cada jugada
                terminalIzq = self.__getDominosEnMesa[0]._getLadoA
                terminalDer = self.__getDominosEnMesa[len(self.__getDominosEnMesa)-1]._getLadoB

                #actualizo la posicion del jugador actual para pasar al siguiente jugador              
                posJugadorActual += 1
                jugadorActual = self.__getJugadores[posJugadorActual]
                
                #jugadaInicial = verifica si el jugador esta realizando un jugada inicial
                jugadaInicial = False
        
        return Ganador, fichaGanadora, passCont, terminalIzq, terminalDer, registroPartidas

    #METODO: ejecuta el juego
    def _jugarDomino(self):

        #inicializo los dominos en la mesa
        self.__crearDominoes
        #guarda el jugador que realizo la jugada ganadora
        Ganador = None

        #Jugar hasta llegar al puntaje propuesto por __jugarHasta
        while self.__getJugadores[0]._getPuntosGanadosJugador < self.__jugarHasta and self.__getJugadores[1]._getPuntosGanadosJugador < self.__jugarHasta and self.__getJugadores[2]._getPuntosGanadosJugador < self.__jugarHasta and self.__getJugadores[3]._getPuntosGanadosJugador < self.__jugarHasta:

            #revuelvo las fichas
            self.__revolverFichas
            #reparto las fichas entre los jugadores
            self.__repartirFichas            
            
            #LLamo al metodo que ejecuta el ciclo de la partida y devuelve la jugada final para luego establecer los resultados
            Ganador, fichaGanadora, passCont, terminalIzq, terminalDer, registroPartidas = self.__ciclosDePartida(Ganador)
                
            #fin de partida, estableciendo la forma en la que gana un jugador
            registroPartidas = self.__finDePartida(Ganador, fichaGanadora, terminalIzq, terminalDer, passCont, registroPartidas)
                
            #muestro resultado de fin de partida
            self.__tablaDeFinDePartida(registroPartidas)

            input("\n\n  FIN de partida...\n  Devolviendo las fichas sobrantes de los jugadores a la mesa...\n  presiona cualquier tecla para seguir jugando....")
        
        for jugador in self.__getJugadores:
            jugador._borrarPuntosGanados
        return Ganador
            