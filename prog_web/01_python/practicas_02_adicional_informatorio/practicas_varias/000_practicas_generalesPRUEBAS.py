
class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.saludar()

    def saludar(self):
        print(f'Hola, soy {self.nombre}! Tengo {self.edad} años.\n')

    def modificar(self, nombre_nuevo = None, edad_nueva = None):
        if nombre_nuevo:
            print(f'Renombrando nombre {self.nombre} a {nombre_nuevo}')
            self.nombre = nombre_nuevo
        if edad_nueva:
            print(f'Cambiando edad {self.edad} a {edad_nueva}')
            self.edad = edad_nueva
        self.saludar()

            

esteban = Persona('Esteban', 29)
esteban.modificar()
esteban.modificar('Carlos')
esteban.modificar('Carloss',25)
esteban.modificar(edad_nueva=30)
esteban.modificar(nombre_nuevo='Estebann', edad_nueva=29)

