
class Persona:
    def __init__(self, dni, nombre, sexo) -> None:
        self.dni = dni
        self.nombre = nombre
        self.sexo = sexo
    def getNombre(self):
        return self.nombre
    def setNombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    # un get y set p/cada atributo

    
    def __str__(self): # sobreescritura de metodos! sirve para el 
                        # print(ObjetoPersona)
        return f"Persona: {self.nombre}, DNI: {self.dni}"

class Alumno(Persona):
    def __init__(self, dni, nombre, sexo, carrera) -> None:
        Persona.__init__(self, dni, nombre, sexo)
        self.carrera = carrera


class Profesor(Persona):
    def __init__(self, dni, nombre, sexo, antiguedad) -> None:
        Persona.__init__(self, dni, nombre, sexo)
        self.antiguedad = antiguedad

prof = Profesor(44000444, "alan", "M", 30)
al = Alumno(55000555, "Maria", "F", "ISI")
print(prof)
print(al)