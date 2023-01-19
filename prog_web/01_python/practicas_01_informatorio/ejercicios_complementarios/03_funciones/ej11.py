# Ejercicio 11: ¿Es un número primo?
# Un número primo es un número entero mayor que 1 que solo es divisible
#  por uno y por sí mismo. Escriba una función que determine si su
#  parámetro es primo o no, devolviendo True si lo es y False en caso
#  contrario. Escriba un programa principal que lea un número entero
#  del usuario y muestre un mensaje que indique si es primo o no.
#  Asegúrese de que el programa principal no se ejecutará si el archivo
#  que contiene su solución se importa a otro programa.

# nota: no se entendio la ultima parte, preguntar en clase
# uso de "clave"? visibilidad de funcion? (func privada??)
# __all__ = ['']

def _its_prime(number_):
    if number_ < 2:
        return False
    for n in range(2, number_):
        if number_%n == 0:
            return False
    return True

print("A continuacion se muestran los numeros primos del 1 al 100")
result = ""

for i in range(100):
    if _its_prime(i):
        result = result + str(f"{i}, ")    
print(result)


#pruebas para importar funciones, pendiente aprender
'''
# importing sys
import sys
# adding Folder_2/subfolder to the system path
sys.path.insert(0, 'D:\CURSOS\Informatorio\ETAPA_2_Desarrollo_Web_2022'
'\Programacion_Web\INFORMATORIO2022\complementarios\\03_funciones')

# importing the hello
from ej11 import *
'''