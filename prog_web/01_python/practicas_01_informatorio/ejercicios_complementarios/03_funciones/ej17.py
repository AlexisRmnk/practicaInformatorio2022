# Ejercicio 17: Conversiones de bases arbitrarias
# Escriba un programa que permita al usuario convertir un número de una
#  base a otra. Su programa debe admitir bases entre 2 y 16 tanto para 
#  el número de entrada como para el número de resultado. Si el usuario
#  elige una base fuera de este rango, se debe mostrar el mensaje de
#  error apropiado y el programa debe salir. Divida su programa en varias
#  funciones, incluida una función que convierte de una base arbitraria
#  a una base 10, una función que convierte de una base 10 a una base
#  arbitraria y un programa principal que lee las bases y el número de
#  entrada del usuario.

def int2hex(int_number: int) -> str:
    '''
    converts an int to hex string (without the 0x prefix)
    '''
    if int_number == 0:
        return "0"
    elif int_number == 1:
        return "1"
    elif int_number == 2:
        return "2"
    elif int_number == 3:
        return "3"
    elif int_number == 4:
        return "4"
    elif int_number == 5:
        return "5"
    elif int_number == 6:
        return "6"
    elif int_number == 7:
        return "7"
    elif int_number == 8:
        return "8"
    elif int_number == 9:
        return "9"
    elif int_number == 10:
        return "A"
    elif int_number == 11:
        return "B"
    elif int_number == 12:
        return "C"
    elif int_number == 13:
        return "D"
    elif int_number == 14:
        return "E"
    elif int_number == 15:
        return "F"
    else:
        print(f"ERROR, el numero {int_number} NO es un numero entero valido.")
        return -1

def hex2int(hex_number: str) -> int:
    '''
    converts an hex string (without the 0x prefix) to int
    '''
    hex_number = hex_number.lower()
    if (hex_number == "0"):
        return 0
    elif (hex_number == "1"):
        return 1
    elif (hex_number == "2"):
        return 2
    elif (hex_number == "3"):
        return 3
    elif (hex_number == "4"):
        return 4
    elif (hex_number == "5"):
        return 5
    elif (hex_number == "6"):
        return 6
    elif (hex_number == "7"):
        return 7
    elif (hex_number == "8"):
        return 8
    elif (hex_number == "9"):
        return 9
    elif (hex_number == "a"):
        return 10
    elif (hex_number == "b"):
        return 11
    elif (hex_number == "c"):
        return 12
    elif (hex_number == "d"):
        return 13
    elif (hex_number == "e"):
        return 14
    elif (hex_number == "f"):
        return 15
    else:
        print(f"ERROR, el numero {hex_number} NO es un numero hexadecimal.")
        return -1

def base_10_to_base_n(number_b10: int, base_n: int) -> str:
    '''
    converts an int (base 10 to string (base n)
    only works with base n = between 2 and 16
    '''
    result = str()
    while(True):
        result = int2hex(number_b10 % base_n) + result
        number_b10 = number_b10 // base_n
        if (number_b10 // base_n) < base_n:
            result = int2hex(number_b10 % base_n) + result
            result = int2hex(number_b10 // base_n) + result
            break
    return result

def base_m_to_base_10(number_bm: str, base_m: int) -> int: 
    '''
    converts an string (base m) to int (base 10)
    only works with base m = between 2 and 16
    '''
    string_ = number_bm
    result = 0
    exponente = len(string_) - 1
    for char_ in string_:
        result = hex2int(char_) * base_m**exponente + result
        if exponente == 0:
            break
        exponente = exponente - 1
    return result

def base_m_to_base_n(number_bm: str, base_m: int, base_n:int) -> str:
    '''
    converts an string (base m) to another string (base n)
    only works with bases between 2 and 16
    '''
    aux1 = base_m_to_base_10(number_bm, base_m)
    result = base_10_to_base_n(aux1, base_n)
    return result

print("Inicio programa")
while(True):
    num = input("Ingresar numero para convertir:\n\t")
    base_m = input(f"Ingresar base del numero {num} (entre 2 y 16). "
        "(Apretar solo ENTER para indicar base 10)\n\t")
    if base_m == "":
        base_m = 10
    base_m = int(base_m)
    if base_m > 16 or base_m < 2:
        print("BASE INGRESADA INCORRECTA - REINICIANDO EJECUCION")
        continue
    base_n = input(f"Ingresar base del numero deseado (entre 2 y 16). "
        "(Apretar solo ENTER para indicar base 10)\n\t")
    if base_n == "":
        base_n = 10
    base_n = int(base_n)
    if base_n > 16 or base_n < 2:
        print("BASE INGRESADA INCORRECTA - REINICIANDO EJECUCION")
        continue
    
    # controls if some value in the number string exceeds the base value
    flag = False
    for n in num:
        if hex2int(n) >= base_m:
            flag = True
    if flag:
        print(f"ERROR - El numero {num} no puede ser de base {base_m}!")
        continue

    result_ = base_m_to_base_n(num, base_m, base_n)
    print(f"El numero {num} (base {base_m}) es {result_} (base {base_n}).")
    x = input("Para ingresar otro numero presione ENTER. Para salir envie "
                "cualquier caracter.\n")
    if x != "":
        break