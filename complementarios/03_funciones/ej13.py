# Ejercicio 13: Contraseña aleatoria
# Escriba una función que genere una contraseña aleatoria. La contraseña
#  debe tener una longitud aleatoria de entre 7 y 10 caracteres. Cada
#  carácter debe seleccionarse al azar de las posiciones 33 a 126 en la
#  tabla ASCII. Su función no tomará ningún parámetro y devolverá la
#  contraseña generada aleatoriamente como su único resultado.
# Desarrolle un programa principal y muestre la contraseña generada
#  aleatoriamente.

# Sugerencia: Probablemente encuentre útil la función chr cuando
#   complete este ejercicio.
import random

def random_password():
    length = random.randint(7, 10)
    string_ = str()
    for i in range(length):
        ascii_ = random.randint(33, 126)
        char_ = chr(ascii_)
        string_ = string_ + str(char_)
    return string_

while(True):
    print()
    x = input('Presione ENTER para generar una password aleatoria'
                ' ("0" para salir)')
    if x == "0":
        break
    r_password = random_password()
    print(f"Password aleatoria de {len(r_password)} caracteres: {r_password}")