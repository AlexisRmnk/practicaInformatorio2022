# Ejercicio 14: Matricula aleatoria

# En una jurisdicción particular, las matrículas más antiguas consisten
#  en tres letras seguidas de tres números. Cuando se utilizaron todas
#  las placas que siguen ese patrón, el formato se cambió a cuatro números
#  seguidos de tres letras. Escriba una función que genere una matrícula
#  aleatoria. Escriba un programa principal que llame a su función y
#  muestre la placa generada al azar.

# nnnnAAA
# ASCII: A 65 --> Z 90

import random

def new_number_plate():
    string_ = str()
    for i in range(4):
        string_ = string_ + str(random.randint(0,9))
    for i in range(3):
        string_ = string_ + chr(random.randint(65,90))
    return string_

while(True):
    print()
    x = input('Presione ENTER para generar una patente aleatoria'
                ' ("0" para salir)\n\t')
    if x == "0":
        break
    r_numb_plate = new_number_plate()
    print(f"Patente aleatoria: {r_numb_plate}")