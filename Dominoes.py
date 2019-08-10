####################################
######### Librerias ################
####################################

# e4from Ficha import *
import sys
from Jugador import Jugador
from Ficha import Ficha
from Funciones import cls
from random import choice
from random import shuffle

####################################
######### Clases ###################
####################################

class Mesa(Ficha, Jugador):

    def __init__(self, modoJuego = "1vs3"):
        self.__jugadores = []
        self.__fichasEnMesa = []
        self.__modoJuego = modoJuego

    ####################################
    ######### SETTERS ##################
    ####################################

    #METODO: crea e inicializa las 28 fichas del domino en la mesa para que se pueda jugar
    @property
    def __iniciarDominoes(self):
        a, b, totalFichas, fichas = 0, 0, 0, []

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
        
    #METODO: revolver las fichas
    @property
    def __revolverFichas(self):
        shuffle(self.__getDominosEnMesa)

    #METODO: reparte las fichas entre los jugadores
    @property
    def __repartirFichas(self):
        
        for jugador in self.__jugadores:
            while jugador._getTotalFichasJugador < 7:
                jugador._addFicha(self.__fichasEnMesa.pop())
    
    #METODO: muestra las fichas jugadas en la mesa de juego
    def __mostrarMesa(self):

        mesa = "Mesa de juego: "
        for ficha in self.__getDominosEnMesa:
            mesa += "{}".format(str(ficha))
        return mesa

    #METODO: muestra y retorna los resultados de cada jugadas
    def __getResultados(self, jugadorActual, ganoPor = "Dominacion"):

        if self.__getModo == "1vs3":

            if ganoPor == "Dominacion":

                totalpuntos = 0
                tablaJugador = "\n Tabla de Jugadores |"
                for jugador in self.__getJugadores:
                    if jugador._getTotalFichasJugador > 0:
                        totalpuntos += jugador._getTotalPuntosJugador                
                        tablaJugador += " {}, Fichas: {}, Puntos: {} |".format(jugador._getNombreJugador, jugador._getFichasDelJugador, jugador._getTotalPuntosJugador)
                    else:
                        tablaJugador += " {}, Ganador! ".format(jugador._getNombreJugador)


                print(tablaJugador)
                print("\n {} Obtiene: {} Puntos \n".format(jugadorActual._getNombreJugador, totalpuntos))
                return "done"       
    
    #METODO: ejecuta el juego
    def jugarDomino(self):
        #inicializo los dominos en la mesa
        self.__iniciarDominoes
        #revuelvo las fichas
        self.__revolverFichas
        #reparto las fichas entre los jugadores
        self.__repartirFichas
        
        #guarda el jugador que realizo la jugada ganadora
        Ganador = ""
        #lleva un conteo de pases para saber cuando el juego esta trancado
        passCont = 0
        #variable jInicial
        jugadaInicial = False
        #lo utilizo para modificar la posicion del jugador en turno
        posJugadorActual = 0
        #pLateral obtiene el valor del terminal izquierdo y derecho de la mesa que se puede hacer jugada
        pLateral,uLateral = None,None
        #lleva un registro de las jugadas total realizadas/ registro de jugadas por ronda
        registroTotal, registroRonda = [],[]
        # sys.exit()

        #El juego se ejecutara mientras que 1 jugador posea fichas o el juego este tranchado
        JUEGO = True
        while JUEGO:

            #limpiador de consola
            cls()

            #Si es la jugada inicial se ejecutara esta condicion
            if len(self.__getDominosEnMesa) == 0:
                #obtengo un jugador aleatorio para la jugada inicial
                jugadorActual = choice(self.__getJugadores)
                #obtengo la posicion del jugador inicial para poder seguir con los otros jugadores
                posJugadorActual = self.__getJugadores.index(jugadorActual)
                jugadaInicial = True
                
 
            if jugadorActual._getStatusJugador == "CPU":

                #recibo la posicion de la jugada y la ficha del metodo Jugar del Jugador CPU
                posJugada, fichaActual = jugadorActual._jugarCPU(pLateral, uLateral, jugadaInicial)

            elif jugadorActual._getStatusJugador == "HM":
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
                       
            #si el jugador hizo una jugada se elimina la ficha del jugador
            if posJugada:

                if passCont == 3:
                    print("{} tiene 30!!".format(jugadorActual._getNombreJugador))
                    registroRonda.append("Jugador: {} consigue 25 por pases!!!".format(Ganador._getNombreJugador))

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

                #TERMINO EL JUEGO
                JUEGO = False
                
                #formas de ganar
                if jugadorActual._getTotalFichasJugador == 0:

                    if pLateral != uLateral and (fichaActual._getLadoA == pLateral and fichaActual._getLadoB == uLateral) or (fichaActual._getLadoA == uLateral and fichaActual._getLadoB == pLateral):
                        registroRonda.append("Jugador: {} Domina con KAPICUA!!!".format(Ganador._getNombreJugador))
                    else:
                        self.__getResultados(jugadorActual, "Dominacion" )
                        registroRonda.append("Jugador: {} Domina!!!".format(Ganador._getNombreJugador))
                
                if passCont == 4:
                    for jugador in self.__getJugadores:
                        if jugadorPuntos(Ganador) > jugadorPuntos(jugador):
                            Ganador = jugador

                    #menosPuntos(self.jugadores[0],self.jugadores[1],self.jugadores[2],self.jugadores[3])
                    registroRonda.append("Jugador: {} Gana por puntos, Juego Trancado !!!".format(Ganador._getNombreJugador))
                
                #concateno el registroRonda al registroTotal
                registroTotal += registroRonda
                    

        #muestro la mesa de juego y el registro de las jugadas/ VISTA SIMPLE
        
        
        for e in registroTotal:
            print(e)
        
        # print()
        # print(self.mostrarMesa())

            
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