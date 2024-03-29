####################################
######### LIBRERIA #################
####################################
from random import choice

####################################
######### CLASE ####################
####################################
class Jugador:

    def __init__(self, nomJugador, status = 'CPU'):
        self.__nombre = nomJugador
        self.__status = status
        self.__fichas = []
        self.__totalFichas = 0
        self.__puntosGanados = 0
        
    ####################################
    ######### SETTERS ##################
    ####################################
    
    #METODO: agrega una ficha a la mano del jugador
    def _setFichas(self, ficha):
        self.__fichas.append(ficha)
        self.__totalFichas += 1
    
    #METODO: guarda el total de puntos que gana el jugador por jugada
    def _setPuntosGanados(self, puntos):
        self.__puntosGanados += puntos
    
    ####################################
    ######### GETTERS ##################
    ####################################
    
    #METODO: retorna el nombre del jugador
    @property
    def _getNombreJugador(self):
        return self.__nombre

    #METODO: retorna la condicion del jugador (CPU|Humano)
    @property
    def _getStatusJugador(self):
        return self.__status

    #METODO: retorna las objFichas del jugador
    @property
    def _getFichasJugador(self):
        return self.__fichas

    #METODO: retorna la cantidad de fichas que posee el jugador
    @property
    def _getTotalFichasJugador(self):
        return self.__totalFichas

    #METODO: retorna la cantidad de puntos ganados por el jugador
    @property
    def _getPuntosGanadosJugador(self):
        return self.__puntosGanados

    #METODO: retorna la cantidad de puntos que existen en las fichas que posee el jugador
    @property
    def _getTotalPuntosJugador(self):
        total = 0

        for ficha in self.__fichas:
            total += (ficha._getLadoA + ficha._getLadoB)
        return total
        
    ####################################
    ######### METODOS ##################
    ####################################

    #METODO: elimina posesion de la ficha jugada y resta 1 al total de fichas del jugador
    def _fichaJugada(self, ficha):
        self.__fichas.remove(ficha)
        self.__totalFichas -= 1
    
    #METODO: limpia los puntos que ha ganado el jugador para iniciar un nuevo juego
    @property
    def _borrarPuntosGanados(self):
        self.__puntosGanados = 0
      
    #METODO: devuelve las fichas no jugadas que posee el jugador 
    @property   
    def _devolverFichasDelJugador(self):
        devolver = []
        while len(self._getFichasJugador) > 0:
            devolver.append(self._getFichasJugador.pop())
            self.__totalFichas -= 1 
        return devolver

    #METODO: retorna una vista detallada de las fichas que posee el jugador
    @property
    def __mostrarOpcionDelJugador(self):
        # listFicha = []
        mano = "\n  | "
        cont = 1

        for e in self._getFichasJugador:
            mano += str(cont) + ":" + str(e) + "  "
            cont+=1
        mano =mano[:len(mano)-1] + "|"
        print(mano) 

    #METODO: Permite al jugador HM realizar una jugada inicial
    @property
    def __jugadaInicialHM(self):

        while True:
                digito = int(input(f"\n  Juega digitando el numero a la izquierda de la ficha (1 al {len(self._getFichasJugador)}): "))
                if digito > 0 and digito <= len(self._getFichasJugador):
                    #retorno la el lado de terminal en cual se jugara la ficha, la ficha                    
                    return "terminalDerecho", self._getFichasJugador[digito-1]
                else:
                    print("\n  Digito fuera de rango, elige de nuevo...")

    #METODO: Permite al jugador HM determinar en cual terminal decea jugar una ficha seleccionada que pueda jugar a ambos lados
    def __jugadaAmbosTerminalesHM(self, terminalIzq, terminalDer, fichaActual):

        while True:
            #el usuario elige el lado
            option = input(f"\n  ATENCION|Puedes jugar a ambos lados: [1->IZQ | 2->DER]: ")
            
            #si el digito ingresado es numerico y es igual a 1 entonces se jugara por la izquierda
            if option.isdigit() and int(option) == 1:
                if terminalIzq == fichaActual._getLadoA:
                    fichaActual._girarFicha()                           
                return "terminalIzquierdo", fichaActual
            
            #si el digito ingresado es numerico y es igual a 1 entonces se jugara por la derecha
            if option.isdigit() and int(option) == 2:
                if terminalDer == fichaActual._getLadoB:
                    fichaActual._girarFicha()                   
                return "terminalDerecho", fichaActual

            #si el digito ingresado no cumple los requisitos imprime este scrip
            print("\n  ATENCION|Tecla fuera de rango, elige de nuevo...")

    #METODO: Permite al jugador HM determinar cual ficha decea jugar y en que terminal
    def __modosDeJugadaHM(self, terminalIzq, terminalDer):

        #ciclo solo retorna
        while True:
            digito = input(f"\n  Juega digitando el numero a la izquierda de la ficha (1 al {len(self._getFichasJugador)}): ")
            # si el digito ingresado por consola es numerico, digito es mayor que cero y digito es menor igual a la cantidad de fichas del jugador
            
            if digito.isdigit() and int(digito) > 0 and int(digito) <= len(self._getFichasJugador):
                #se obtiene la ficha que se va a jugar
                fichaActual = self._getFichasJugador[int(digito)-1]
                
                #si los terminales de la mesa no son iguales y cada lado de la ficha a jugar es igual a ambos terminales, el usuario decide en que lado quiere jugar
                if (terminalIzq != terminalDer) and ((fichaActual._getLadoA == terminalIzq and fichaActual._getLadoB == terminalDer) or (fichaActual._getLadoA == terminalDer and fichaActual._getLadoB == terminalIzq)): 

                    #llamo el metodo que me permite jugar una ficha a ambos lados
                    return self.__jugadaAmbosTerminalesHM(terminalIzq, terminalDer, fichaActual)   
                
                #si el jugador decide jugar una ficha que se jugara por el terminal derecho, ejecuta este script        
                elif terminalDer == fichaActual._getLadoA or terminalDer == fichaActual._getLadoB:

                    #esta condicion permite voltear la ficha de ser necesario
                    if terminalDer == fichaActual._getLadoB:
                        fichaActual._girarFicha()    

                    #retorno el terminal en el que se jugara la ficha y la ficha a jugar
                    return "terminalDerecho", fichaActual

                #si el jugador decide jugar una ficha que se jugara por el terminal izquierdo, ejecuta este script        
                elif terminalIzq == fichaActual._getLadoA or terminalIzq == fichaActual._getLadoB:       
                    
                    #esta condicion permite voltear la ficha de ser necesario
                    if terminalIzq == fichaActual._getLadoA:
                        fichaActual._girarFicha()                         

                    #retorno el terminal en el que se jugara la ficha y la ficha a jugar
                    return "terminalIzquierdo", fichaActual

                #si el jugador elige una ficha que no se puede jugar, ejecuta este comentario
                print("\n  ATENCION|Ficha no se puede jugar, elige de nuevo...")     
            else:
                #si el jugador elige un numero o letra que no es acorde con las posiciones de las fichas, ejecuta este comentario
                print("\n  ATENCION|Tecla fuera de rango, elige de nuevo...")

    #METODO: Permite al usuario humano realizar una jugada
    def _jugarHM(self, terminalIzq, terminalDer, jugadaInicial):

        #muestra la vista detallada
        self.__mostrarOpcionDelJugador

        #verifico si es una jugada inicial/retorno
        if jugadaInicial:

            #como es una jugada inicial retorno la posicion y la ficha a jugar
            posJugada, fichaActual = self.__jugadaInicialHM
            self._fichaJugada(fichaActual)
            return posJugada, fichaActual

        #verifico si el jugador posee fichas que pueda jugar        
        for ficha in self._getFichasJugador:
            #si el jugador posee fichas que pueda jugar se validad la condicion de lo contrario el jugador pasara
            if terminalDer == ficha._getLadoA or terminalDer == ficha._getLadoB or terminalIzq == ficha._getLadoA or terminalIzq == ficha._getLadoB:
                #recibo la ficha seleccionada por el jugador
                posJugada, fichaActual = self.__modosDeJugadaHM(terminalIzq, terminalDer)
                #elimino la ficha jugada de la posecion de fichas del jugador
                self._fichaJugada(fichaActual)
                #retorno la ficha jugada
                return posJugada, fichaActual 
        #si el jugador no posee fichas que se puedan jugar el jugador retorna pase
        input("\n  ATENCION|No posees fichas que puedas jugar, presiona cualquier tecla para continuar...")
        return None, "PASS"


    #Jugada realizada por jugador CPU
    def _jugarCPU(self, terminalIzq, terminalDer, jugadaInicial = False):
        
        #se verifica que exista por lo menos una jugada previa para realizar las verificaciones de lugar de lo contrario el jugador jugara una al azar
        if not jugadaInicial:
            
            for ficha in self._getFichasJugador:

                #verifico que el terminal derecho de la mesa existe en las fichas del jugador
                if terminalDer == ficha._getLadoA or terminalDer == ficha._getLadoB:
                   
                    #si la ficha existente esta del lado incorrecto al que se puede jugar, la ficha se voltea
                    if terminalDer == ficha._getLadoB:
                        ficha._girarFicha()
                    
                    self._fichaJugada(ficha)        
                    return "terminalDerecho", ficha

                #verifico que el terminal izquierdo de la mesa existe en las fichas del jugador
                if terminalIzq == ficha._getLadoA or terminalIzq == ficha._getLadoB:

                    #si la ficha existente esta del lado incorrecto al que se puede jugar, la ficha se voltea                     
                    if terminalIzq == ficha._getLadoA:
                        ficha._girarFicha()

                    self._fichaJugada(ficha)                            
                    return "terminalIzquierdo", ficha
           
            #de no encontrarse la ficha en la mano de el jugador retorno Pass
            return None, "PASS"
                
        else:
            #obtiene una ficha aleatoria, establece la posicion que se jugara la ficha elegida
            fichaActual = choice(self._getFichasJugador)
            
            self._fichaJugada(fichaActual)        
            return "terminalDerecho", fichaActual