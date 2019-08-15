####################################
######### CLASE ####################
####################################
class Ficha:

    def __init__(self, a, b):
        self.__ladoA = a
        self.__ladoB = b
        self.__ficha = [self.__ladoA, self.__ladoB]
    
    ####################################
    ######### GETTERS ##################
    ####################################

    #METODO: retorna el lado A o 0 de la ficha
    @property
    def _getLadoA(self):
        return self.__ladoA

    #METODO: retorna el lado B o 1 de la ficha
    @property
    def _getLadoB(self):
        return self.__ladoB

    #METODO: retorna el objFicha
    @property
    def _getFicha(self):
        return self.__ficha

    #METODO: intercambia los valores de la ficha
    def _girarFicha(self):

        #se realizo para que sea mas entendible el cambio
        self.__ladoA, self.__ladoB = self.__ladoB, self.__ladoA
        #se asignan nuevos valores a la lista
        self.__ficha = [self.__ladoA, self.__ladoB]
        
    #METODO: imprime la ficha
    def __str__(self):
        return "{}".format(self.__ficha)

