# Las palabras como primero, segundo y tercero se refieren a números
#  ordinales. En este ejercicio, escribirá una función que toma un
#  número entero como su único parámetro y devuelve una cadena que
#  contiene el número ordinal apropiado como único resultado. Su función
#  debe manejar los enteros entre 1 y 12 (inclusive). Debería devolver
#  una cadena vacía si se proporciona un valor fuera de este rango como
#  parámetro. Incluya un programa principal que utilice su función
#  mostrando cada número entero del 1 al 12 y su número ordinal.

def ordinal(number):
    if(number == 1):
        return "Primero"
    elif(number == 2):
        return "Segundo"
    elif(number == 3):
        return "Tercero"
    elif(number == 4):
        return "Cuarto"
    elif(number == 5):
        return "Quinto"
    elif(number == 6):
        return "Sexto"
    elif(number == 7):
        return "Septimo"
    elif(number == 8):
        return "Octavo"
    elif(number == 9):
        return "Noveno"
    elif(number == 10):
        return "Decimo"
    elif(number == 11):
        return "Undecimo"
    elif(number == 12):
        return "Duoecimo"
    else:
        return ""

print('Ingrese un numero entre 1 y 12 para "traducirlo" a n° ordinal:')
number_ = int(input("\t"))
string_ = ordinal(number_)

if string_ != "":
    print(f"El valor ordinal del numero {number_} es: {string_}")
else:
    print("Se ingreso un valor incorrecto.")