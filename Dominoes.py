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

####################################################################################################

class Jugador:

    def __init__(self, nomJugador):
        self.nombre = nomJugador
        self.fichas = []
        self.totalFichas = 0

    #se llama este metodo si el jugador necesita una ficha aparte de las que reparte la mesa(cuando se juege de 2)
    # def addFicha(self, ficha):
    #     self.fichas = ficha
    #     self.totalFichas += 1
    
    #realiza la jugada en la mesa como haria cada jugador
    def Jugar(self, fichasEnMesa, pLateral, uLateral):
        
        #se verifica que exista por lo menos una jugada previa para realizar las verificaciones de lugar de lo contrario el jugador jugara una al azar
        if len(fichasEnMesa) > 0:
            
            #establece la posicion en la que se jugara la ficha
            posfichaActual = None
            #guarda temporalmente la ficha que se jugara
            fichaActual = None

            for ficha in self.fichas:

                #verifico que el terminal derecho de la mesa existe en las fichas del jugador
                if uLateral == ficha.ladoA or uLateral == ficha.ladoB:
                   
                    #si la ficha existente esta del lado incorrecto al que se puede jugar, la ficha se voltea
                    if uLateral == ficha.ladoB:
                        ficha.girar()
                    
                    fichaActual = ficha
                    posfichaActual = "uLateral"

                    self.fichas.remove(ficha)
                    self.totalFichas -= 1

                    #retorno la el lado de terminal en cual se jugara la ficha, la ficha                    
                    return posfichaActual, fichaActual

                #verifico que el terminal izquierdo de la mesa existe en las fichas del jugador
                if pLateral == ficha.ladoA or pLateral == ficha.ladoB:

                    #si la ficha existente esta del lado incorrecto al que se puede jugar, la ficha se voltea                     
                    if pLateral == ficha.ladoA:
                        ficha.girar()
                    
                    fichaActual = ficha
                    posfichaActual = "pLateral"

                    self.fichas.remove(ficha)
                    self.totalFichas -= 1
                    
                    #retorno la el lado de terminal en cual se jugara la ficha, la ficha
                    return posfichaActual, fichaActual
           
            #de no encontrarse la ficha en la mano de el jugador retorno Pass
            return None, "PASS"
                
        else:
            #obtiene una ficha aleatoria, establece la posicion que se jugara la ficha elegida
            fichaActual = random.choice(self.fichas)
            posfichaActual = "uLateral"
            
            #remueve la ficha jugada del jugador
            self.fichas.remove(fichaActual)
            self.totalFichas -= 1
            
            #retorna la posicion y la ficha
            return posfichaActual, fichaActual

    #muestra las fichas que posee el jugador
    def fichasDelJugador(self):

        listFicha = []
        for e in self.fichas:
            listFicha.append(str(e))

        return "{} tiene: {}".format(self.nombre, listFicha)


######################################################################################################
#creando la estructura de la mesa de juego
#DONE la mesa revuelve las fichas
#DONE la mesa reparte las fichas
#DONE la mesa asigna el turno al jugador
#DONE la mesa mantiene un registro de fichas jugadas
#DONE la mesa tiene un metodo jugar donde se desarrolla todo el juego de domino y sera el metodo que se llamara para ejecutar el juego 
#DONE la mesa mantiene un registro de el primer valor de ficha jugada y el ultimo valor de ficha jugada [A|B][B|C][C|D] => V1 = A, V2 = D, esto para saber en que posicion podemos jugar la nueva ficha 

class Mesa():

    #guardando todas las fichas en una variable de clase para que pueda ser accedida su informacion desde todos los objetos 
    #fichas = crearDominoes()
    
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
        #lleva un registro de las jugadas realizadas
        registro =[]
        #lleva un conteo de pases para saber cuando el juego esta trancado
        passCont = 0

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
                Ganador = jugadorActual.nombre
            
            #determina que el jugador jugara por el terminal izquierdo
            if (posJugada == "pLateral"):
                
                passCont = 0
                self.dominoesEnMesa.insert(0, fichaActual)
                Ganador = jugadorActual.nombre
            
            #registro la jugada realizada
            registro.append("Jugador: {} jugo: {}".format(jugadorActual.nombre, fichaActual))
            
            #actualizo el valor de los terminales de la mesa de jugo despues de cada jugada
            pLateral = self.dominoesEnMesa[0].ladoA
            uLateral = self.dominoesEnMesa[len(self.dominoesEnMesa)-1].ladoB

            if jugadorActual.totalFichas != 0 and passCont != 4:
                #actualizo la posicion del jugador actual despues de cada ronda
                if posJugadorActual == 3:
                    posJugadorActual = -1

                #actualizo la posicion del jugador actual para pasar al siguiente jugador
                posJugadorActual += 1
                jugadorActual = self.jugadores[posJugadorActual]

            else:
                registro.append("Jugador: {} Es el Ganador!!!".format(Ganador))
                partida = False

        #muestro la mesa de juego y el registro de las jugadas
        print()
        print(self.mostrarMesa())
        print()
        for e in registro:
            print(e)

            
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

print("estamos en la mesa de jugo")
mesa.playDomino()

### IDEAS ### 
## LA MESA recibe los jugadores como parametros para iniciar el juego
## Mesa(jugador1, jugador2)
#AminMoya001
#829-645-2685
#si se juega de 2, poner una variable como reserva de las fichas restante y adicionarle el revolver simulando cojida de ficha aleatoria, ya que se utilizara el pop() para obtenerla