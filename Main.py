####################################
######### LIBRARIES ################
####################################
from Dominoes import *
####################################
######### CLASS ################
####################################

class Menu(Mesa):

    #METODO: ejecuta la opcion HMvsCPUs
    def __setNombresHMvsCPUs(self, tab, enter):
        #limpio la pantalla
        cls()
        banner()
        #recibo el nombre del jugador
        hmName = input(f"{enter}{tab[0:-1]}Nombre del jugador (Default = 'Guess'): ")

        #si existe el nombre del jugador lo incluyo en la lista de jugadores, de lo contrario coloco Guess en su lugar
        if hmName:
            players = [[hmName,"HM"],["Pedro", "CPU"],["Jose", "CPU"],["Mario", "CPU"]]
        else:
            players = [["Guess","HM"],["Pedro", "CPU"],["Jose", "CPU"],["Mario", "CPU"]]
        
        return players
    
    #METODO: ejecuta hasta cuantos puntos se desarrollara el juego
    def __playTo(self, tab, enter):
        #limpio la pantalla
        cls()
        banner()

        playTo = [100, 150, 200]
        choice = input(f"{enter}{tab[0:-2]}Juego hasta: | 1-> 100 puntos | 2-> 150 puntos | 3->200 puntos | ")

        while True:
            if choice!="" and int(choice) > 0 and int(choice) <= 3:
                return playTo[int(choice)-1]
            
            #limpio la pantalla
            cls()
            banner()
            print(f"{enter}{tab[0:-2]}Digito fuera de rango, favor elige de nuevo...")
            choice = input(f"{tab[0:-2]}Juego hasta: | 1-> 100 puntos | 2-> 150 puntos | 3->200 puntos | ")

    #METODO: ejecuta el ciclo de juego del modo de jugego HMvsCPUs
    def __cicloDeJuegoHMvsCPUs(self, tab, enter):
        
        Mesa._setRegistrarJugadores(self,self.__setNombresHMvsCPUs(tab, enter))
        Mesa._setModoJuego(self,"1vs3")
        
        #mientras el jugador quiera seguir jugando
        GAME = True
        while GAME:
            # self,self.__playTo(tab, enter)
            Mesa._setJugarHasta(self,self.__playTo(tab, enter))
            Ganador = Mesa._jugarDomino(self)
            
            cls()
            banner()
            print(f"{enter}{tab[0:-1]}**************************************")
            print(f"{tab}*   GANADOR {Ganador._getNombreJugador} *")
            print(f"{tab[0:-1]}**************************************")

            option = input(f"{tab[0:-4]} PRESIONE CUALQUIER TECLA PARA VOLVER A JUGAR, DE LO CONTRARIO PRESIONE ( 1 ) PARA SALIR...: ")

            if option =="1":
                GAME = False
        return "Done"

    #METODO: ejecuta el juego    
    def startGame(self):

        #limpio la pantalla
        cls()
        banner()

        #auxiliar para los saltos de linea
        enter = auxEnter(5)
        #auxiliar para uso de tabs
        tab = auxTab(35)

        print(f"{enter}{tab[0:-1]} BIENVENIDO AL MENU DE JUEGO DE DOMINÓ: \n\n\n\n{tab} 1-> HM vs CPUs\n\n{tab} 00-> SALIR DEL JUEGO\n\n\n")
        digito = input(f"{tab[0:-1]} Digite el numero de la opcion a realizar: ")

        while digito != "00":
            
            #HMvsCPUs
            if digito == "1":
                
                #ejecuta el ciclo de juego 
                self.__cicloDeJuegoHMvsCPUs(tab, enter)

            cls()
            banner()
            print(f"{enter}{tab[0:-1]} BIENVENIDO AL MENU DE JUEGO DE DOMINÓ: \n\n\n\n{tab} 1-> HM vs CPUs\n\n{tab} 00-> SALIR DEL JUEGO\n\n\n")
            digito = input(f"{tab[0:-1]} Digite el numero de la opcion a realizar: ")



###############################################
########### EJECUCION DEL PROGRAMA ############
###############################################

menu = Menu()
menu.startGame()
