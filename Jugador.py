####################################
######### Librerias ################
####################################
import random
from Ficha import *

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
    
    def jugarHM(self, pLateral, uLateral,jugadaInicial):

        print("\n\n\n  Mis fichas: ",self.fichasDelJugador())

        if jugadaInicial:
            
            while True:
                digito = int(input(f"\n  Elige la ficha presionando digitos 1 al {len(self.fichas)} de acuerdo a la posicion: "))
                if digito > 0 and digito <= len(self.fichas):
                    #retorno la el lado de terminal en cual se jugara la ficha, la ficha                    
                    return "uLateral", self.fichas[digito-1]
                else:
                    print("\n  Digito fuera de rango, elige de nuevo...")
        
        for ficha in self.fichas:

            #verifico que el terminal derecho de la mesa existe en las fichas del jugador
            if uLateral == ficha.ladoA or uLateral == ficha.ladoB or pLateral == ficha.ladoA or pLateral == ficha.ladoB:

                while True:
                    digito = int(input(f"\n  Elige la ficha presionando digitos 1 al {len(self.fichas)} de acuerdo a la posicion: "))

                    if digito > 0 and digito <= len(self.fichas):
                        fichaActual = self.fichas[digito-1]

                        if (fichaActual.ladoA == pLateral and fichaActual.ladoB == uLateral) or (fichaActual.ladoA == uLateral and fichaActual.ladoB == pLateral) and pLateral != uLateral:                                
                            option = int(input(f"\n  ATENCION|Puedes jugar a ambos lado: Izquierda(1), Derecha(2): "))
                            
                            if option == 1:                              
                                if pLateral == fichaActual.ladoA:
                                    fichaActual.girar()                           
                                # retorno la el lado de terminal en cual se jugara la ficha, la ficha
                                return "pLateral", fichaActual

                            elif option == 2:
                                #si la ficha existente esta del lado incorrecto al que se puede jugar, la ficha se voltea
                                if uLateral == fichaActual.ladoB:
                                    fichaActual.girar()

                                #retorno la el lado de terminal en cual se jugara la ficha, la ficha                    
                                return "uLateral", fichaActual
                              
                        elif uLateral == fichaActual.ladoA or uLateral == fichaActual.ladoB:
                            
                            #si la ficha existente esta del lado incorrecto al que se puede jugar, la ficha se voltea
                            if uLateral == fichaActual.ladoB:
                                fichaActual.girar()

                            #retorno la el lado de terminal en cual se jugara la ficha, la ficha                    
                            return "uLateral", fichaActual

                        elif pLateral == fichaActual.ladoA or pLateral == fichaActual.ladoB:
                            #si la ficha existente esta del lado incorrecto al que se puede jugar, la ficha se voltea                     
                            if pLateral == fichaActual.ladoA:
                                fichaActual.girar()
                            
                            # retorno la el lado de terminal en cual se jugara la ficha, la ficha
                            return "pLateral", fichaActual

                        print("\n  ATENCION|Ficha no se puede jugar, elige de nuevo...")     
                    else:
                        print("\n  ATENCION|Tecla fuera de rango, elige de nuevo...")

        input("\n  ATENCION|No posees fichas que puedas jugar, presiona cualquier tecla para continuar...")
        return None, "PASS"


    #Jugada realizada por jugador CPU
    def jugarCPU(self, pLateral, uLateral, jugadaInicial = False):
        
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

