# clases practica
# usar CamelCase




## PRACTICA

# clase estudiante y clase profesor

class EstudianteUniversitario:
    def __init__(self, Nombre, Legajo, Carrera):
        self.name = Nombre
        self.lu = Legajo
        self.carrera = Carrera
    
    def devolver_datos(self):
        return self.name, self.lu, self.carrera


def menu():
    while(True):
        print("Seleccione opcion:")
        print("1) Cargar estudiante")
        print("2) Ver estudiantes cargados")
        print("0) Salir")
        x = input("\t")
        if x in ("0","1","2"):
            return x
        else:
            print("Valor incorrecto, reintentar.")
            continue

# experimento de funcion recursiva X
def cargar_estudiante(estudiantes_):
    while(True):
        name = input("Indicar nombre de estudiante:")
        lu = input("Indicar legajo de estudiante:")
        career = input("Indicar carrera de estudiante:")
        estudiante_ = EstudianteUniversitario(name, lu, career)
        estudiantes_.append(estudiante_)
        x = input("\nDesea cargar otro estudiante? (ENTER PARA SI, 'N' para"
                    " NO\n\t")
        if x.upper() == "N":
            return estudiantes_
        else:
            continue
        #cargar_estudiante(estudiantes_)

def mostrar_estudiantes(estudiantes1): # list[EstudianteUniversitario]
    print("Informacion de estudiantes:")
    for objEstudiante in estudiantes1:
        tuple_ = objEstudiante.devolver_datos()
        print(f"Nombre: {tuple_[0]}, legajo universitario: {tuple_[1]}"
                f", {tuple_[2]}.")
        

estudiantes = list() # list[EstudianteUniversitario]
have_students = False
while(True):
    select = menu()
    if select == "1":
        estudiantes = cargar_estudiante(estudiantes)
        have_students = True
    elif select == "2":
        if have_students:
            mostrar_estudiantes(estudiantes)
        else:
            print("No hay estudiantes cargados")
    elif select == "0":
        print("Saliendo del programa")
        break
    # pendiente 
  





# for i in range(3):
#     print(f"Estudiante {i+1}:")
#     name = input("Name: ")
#     legajoo = input("Legajo: ")
#     carrera = input("carreraa: ")
#     estudiante = EstudianteUniversitario(name, legajoo, carrera)

# for i in range(3):
#     print(f"legajo de estudiante {i+1}:")
#     print(estudiante1.devolver_legajo())