####################################
######### Librerias ################
####################################
import random

class Jugador:

    def __init__(self, nomJugador, status = 'CPU'):
        self.nombre = nomJugador
        self.fichas = []
        self.totalFichas = 0
        self.status = status

    #se llama este metodo si el jugador necesita una ficha aparte de las que reparte la mesa(cuando se juege de 2)
    # def addFicha(self, ficha):
    #     self.fichas = ficha
    #     self.totalFichas += 1
    
    def jugarHM(self):
        pass


    #Jugada realizada por jugador CPU
    def jugarCPU(self, fichasEnMesa, pLateral, uLateral, jugadaInicial = False):
        
        #se verifica que exista por lo menos una jugada previa para realizar las verificaciones de lugar de lo contrario el jugador jugara una al azar
        if not jugadaInicial:
            
            for ficha in self.fichas:

                #verifico que el terminal derecho de la mesa existe en las fichas del jugador
                if uLateral == ficha.ladoA or uLateral == ficha.ladoB:
                   
                    #si la ficha existente esta del lado incorrecto al que se puede jugar, la ficha se voltea
                    if uLateral == ficha.ladoB:
                        ficha.girar()

                    #retorno la el lado de terminal en cual se jugara la ficha, la ficha                    
                    return "uLateral", ficha

                #verifico que el terminal izquierdo de la mesa existe en las fichas del jugador
                if pLateral == ficha.ladoA or pLateral == ficha.ladoB:

                    #si la ficha existente esta del lado incorrecto al que se puede jugar, la ficha se voltea                     
                    if pLateral == ficha.ladoA:
                        ficha.girar()
                    
                    #retorno la el lado de terminal en cual se jugara la ficha, la ficha
                    return "pLateral", ficha
           
            #de no encontrarse la ficha en la mano de el jugador retorno Pass
            return None, "PASS"
                
        else:
            #obtiene una ficha aleatoria, establece la posicion que se jugara la ficha elegida
            fichaActual = random.choice(self.fichas)
            posfichaActual = "uLateral"
                        
            #retorna la posicion y la ficha
            return posfichaActual, fichaActual

    #muestra las fichas que posee el jugador
    def fichasDelJugador(self):

        listFicha = []
        for e in self.fichas:
            listFicha.append(str(e))

        return "{}".format(listFicha)
