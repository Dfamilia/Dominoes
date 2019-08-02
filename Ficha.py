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