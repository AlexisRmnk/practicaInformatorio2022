# 1 - Crea al menos un objeto de cada subclase y añadelos a una lista llamada
#  vehiculos.

# 2 - Realiza una función llamada catalogar() que reciba la lista de vehículos y
#  los recorra mostrando el nombre de su clase y sus atributos.

# 3 - Modifica la función catalogar() para que reciba un argumento optativo ruedas,
#  haciendo que muestre únicamente los que su número de ruedas concuerde con el
#  valor del argumento. También debe mostrar un mensaje "Se han encontrado {}
#  vehículos con {} ruedas:" únicamente si se envía el argumento ruedas. Ponla
#  a prueba con 0, 2 y 4 ruedas como valor..

# Nota: Puedes utilizar el atributo especial de clase name para recuperar el
#  nombre de la clase de un objeto:
# type(objeto).__name__

from clases_desaf02 import *
from defs_desaf02 import *

# 1)
vehiculos = list()
# subclases: Coche, Camioneta, Bicicleta y Motocicleta
co = Coche("azul", 4, 120, "x")
ca = Camioneta("rojo", 4, 80, "y", 1000)
bi = Bicicleta("azul", 2, "BMX")
moto = Motocicleta("Negro", 2, "Zanella", 75, "z")
vehiculos.append(co)
vehiculos.append(ca)
vehiculos.append(bi)
vehiculos.append(moto)
            
catalogar2(vehiculos)
for ruedas_ in range(0, 5, 2): # 0, 2, 4
    print(f"\nPrueba funcion catalogar con {ruedas_} ruedas:")
    catalogar2(vehiculos, ruedas_)

