# Clase Vehiculo: color, ruedas
# Clase Coche: velocidad, cilindrada
# A partir del siguiente diagrama de clases,
#  implementá clases y métodos para mostrar atributos..

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    # setters y getters
    def getColor(self):
        return self.color
    def getRuedas(self):
        return self.ruedas
    def setColor(self, color_nuevo):
        self.color = color_nuevo
    def setRuedas(self, ruedas_nuevas):
        self.ruedas = ruedas_nuevas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def getVelocidad(self):
        return self.velocidad
    def setVelocidad(self, velocidad_nuevo):
        self.velocidad = velocidad_nuevo
    def getCilindrada(self):
        return self.cilindrada
    def setCilindrada(self, nueva_cilindrada):
        self.cilindrada = nueva_cilindrada
        
    def get_a1(self):
        return self.a1
    def get_b2(self):
        return self.b2
    def get_c3(self):
        return self.c3

    def set_a1(self, a1):
        self.a1 = a1
    def set_b2(self, b2):
        self.b2 = b2
    def set_c3(self, c3):
        self.c3 = c3
