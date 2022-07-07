# Vehiculo: color, ruedas
# Coche: velocidad, cilindrada
# Camioneta: carga

# Vehiculo: color, ruedas
# Bicicleta: tipo
# Motocicleta: velocidad, cilindrada


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

    def getValores(self):
        return f"Ruedas: {self.ruedas}, Color: {self.color} "

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
    
    def getValores(self):
        return (super().getValores() + f"Velocidad: {self.velocidad}, "
                f"cilindrada: {self.cilindrada} ")

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
    def getCarga(self):
        return self.carga
    def setCarga(self, carga_nueva):
        self.carga = carga_nueva
    def getValores(self):
        return super().getValores() + f"Carga: {self.carga} "

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def getTipo(self):
        return self.tipo
    def setTipo(self, tipo_nuevo):
        self.tipo = tipo_nuevo
    def getValores(self):
        return super().getValores() + f"Tipo: {self.tipo} "
    
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)    
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def getVelocidad(self):
        return self.velocidad
    def setTipo(self, velocidad_nuevo):
        self.velocidad = velocidad_nuevo      

    def getCilindrada(self):
        return self.cilindrada
    def setCilindrada(self, cilindrada_nuevo):
        self.cilindrada = cilindrada_nuevo
    def getValores(self):
        return (super().getValores() + f"Velocidad: {self.velocidad}, "
                f"Cilindrada: {self.cilindrada} ")


