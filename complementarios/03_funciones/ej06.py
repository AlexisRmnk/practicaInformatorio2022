# Ejercicio 6: Centrar una cadena en la terminal
# Escriba una función que tome una cadena de caracteres como primer
#  parámetro y el ancho de la terminal en caracteres como segundo
#  parámetro. Su función debe devolver una nueva cadena que consta de
#  la cadena original y el número correcto de espacios iniciales para
#  que la cadena original aparezca centrada dentro del ancho proporcionado
#  cuando se imprima. No agregue ningún carácter al final de la cadena.
#  Incluya un programa principal que use su función.

def center_(string1, window_width1):
    characters_s1 = len(string1)
    initial_space_n = (window_width1 - characters_s1) // 2
    new_string1 = initial_space_n * " " + string1
    return new_string1

print("Ingrese ancho de la ventana (209 en pantalla grande - 148 en"
            " pantalla chica)")
window_width_ = int(input("\t"))
while(True):
    print("Ingrese cadena de caracteres")
    string_ = input("\t")

    print("-" * window_width_)
    print("Cadena centrada:")
    print(center_(string_, window_width_))

    print("\n¿Desea ingresar otra cadena para centrar?")
    print("Ingrese 'N' para salir, cualquier otra tecla para continuar:")
    exit1 = input("\t").upper()
    if exit1 == "N":
        break
    print("-" * window_width_)