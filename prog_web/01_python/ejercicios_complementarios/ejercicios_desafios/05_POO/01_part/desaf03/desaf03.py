# Desarrollar un programa que cargue los datos de un triángulo.
# Implementar una clase con los métodos para inicializar los atributos,
# imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que
# es (equilátero, isósceles o escaleno).

from class_desaf03 import *
from defs_desaf03 import *

i = 1
while(True):
    print(f"Ingrese los datos del triangulo {i}:\n(ENTER para continuar,"
          " '0' para salir)")
    x = input("\t")
    if x == "0":
        break
    s1, s2, s3 = ask_sides()
    t = Triangle(s1, s2, s3)
    t.type()
    i+=1
    print("")