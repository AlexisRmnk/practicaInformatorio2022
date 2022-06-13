# Ejercicio 16: Dígitos hexadecimales y decimales
# Escriba dos funciones, hex2int e int2hex, que conviertan entre dígitos
#  hexadecimales (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E y F) y
#  enteros de base 10. La función hex2int es responsable de convertir
#  una cadena que contiene un solo dígito hexadecimal en un entero de
#  base 10, mientras que la función int2hex es responsable de convertir
#  un entero entre 0 y 15 en un solo dígito hexadecimal. Cada función
#  tomará el valor para convertir como su único parámetro y devolverá
#  el valor convertido como el único resultado de la función. Asegúrese
#  de que la función hex2int funcione correctamente para letras
#  mayúsculas y minúsculas. Sus funciones deberían finalizar el programa
#  con un mensaje de error significativo si se proporciona un parámetro
#  no válido.

def hex2int(hex_number):
    hex_number = hex_number.lower()
    if (hex_number == "0x0"):
        return 0
    elif (hex_number == "0x1"):
        return 1
    elif (hex_number == "0x2"):
        return 2
    elif (hex_number == "0x3"):
        return 3
    elif (hex_number == "0x4"):
        return 4
    elif (hex_number == "0x5"):
        return 5
    elif (hex_number == "0x6"):
        return 6
    elif (hex_number == "0x7"):
        return 7
    elif (hex_number == "0x8"):
        return 8
    elif (hex_number == "0x9"):
        return 9
    elif (hex_number == "0xa"):
        return 10
    elif (hex_number == "0xb"):
        return 11
    elif (hex_number == "0xc"):
        return 12
    elif (hex_number == "0xd"):
        return 13
    elif (hex_number == "0xe"):
        return 14
    elif (hex_number == "0xf"):
        return 15
    else:
        print(f"Error, el numero {hex_number} NO es un numero hexadecimal.")
        return -1

def int2hex(int_number):
    if int_number == 0:
        return "0x0"
    elif int_number == 1:
        return "0x1"
    elif int_number == 2:
        return "0x2"
    elif int_number == 3:
        return "0x3"
    elif int_number == 4:
        return "0x4"
    elif int_number == 5:
        return "0x5"
    elif int_number == 6:
        return "0x6"
    elif int_number == 7:
        return "0x7"
    elif int_number == 8:
        return "0x8"
    elif int_number == 9:
        return "0x9"
    elif int_number == 10:
        return "0xA"
    elif int_number == 11:
        return "0xB"
    elif int_number == 12:
        return "0xC"
    elif int_number == 13:
        return "0xD"
    elif int_number == 14:
        return "0xE"
    elif int_number == 15:
        return "0xF"
    else:
        print(f"Error, el numero {string_} NO es un numero hexadecimal.")
        return -1

string_ = input("Ingrese valor hexadecimal entre 0 y F para convertir en "
                "entero:\n\t")
string_1 = "0x" + string_
hex_to_int = hex2int(string_1) 
string_2 = "0x" + string_.upper()
if hex_to_int != -1:
    print(f"Numero {string_2} pasado a entero: {hex_to_int}")

string_ = input("\nIngrese valor entero entre 0 y 15 para convertir en "
                "hexadecimal: \n\t")
int_to_hex = int2hex(int(string_))

if int_to_hex != -1:
    print(f"Numero {string_} pasado a hexadecimal: {int_to_hex}")