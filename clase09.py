# hacer: calculadora con ciclo iterativo
# por cada vez que quiera terminar la ejecucion, va a tener un MENU
# primero va a ingresar 2 valores y luego poner que quiere hacer con
#  esos 2 valores

def suma(a, b):
    '''SUMA 2 VALORES'''
    return(a + b)

def resta(a, b):
    '''RESTA 2 VALORES'''
    return(a - b)

def multiplicacion(a, b):
    '''MULTIPLICA 2 VALORES'''
    return(a * b)

def division(a, b):
    '''REALIZA DIVISION ENTRE 2 VALORES'''
    return(a / b)

def division_ent(a , b):
    '''REALIZA DIVISION ENTERA ENTRE 2 VALORES'''
    return (a // b)

def potencia(a, b):
    '''REALIZA POTENCIA ENTRE 2 VALORES'''
    return (a ** b)


print("Ingrese dos valores A y B")
a = float(input("Ingrese valor A: "))
b = float(input("Ingrese valor B: "))

while(True):
    print(f"A vale {a}, B vale {b}.")
    print("\nIngrese opcion:\t0 - SALIR")
    print("1 - SUMAR, 2 - RESTAR, 3 - MULTIPLICAR, 4 - DIVISION, "
            "5 - DIVISION ENTERA, 6 - POTENCIA, 7 - REDEFINIR A y B: ")
    x = int(input("\t"))
    if (x == 0):
        break
    elif(x == 1):
        print(f"{a} + {b} = {round(suma(a, b), 2)}")
    elif(x == 2):
        print(f"{a} - {b} = {round(resta(a, b), 2)}")
    elif(x == 3):
        print(f"{a} * {b} = {round(multiplicacion(a, b), 2)}")
    elif(x == 4):
        if (b == 0):
            print("ERROR - B no puede ser 0! redefinir B:")
            b = float(input("Nuevo valor para B: "))
            print("///////////////////////////////////////////////////")
            continue
        print(f"{a} / {b} = {round(division(a, b), 2)}")
    elif(x == 5):
        if (b == 0):
            print("ERROR - B no puede ser 0! redefinir B:")
            b = float(input("Nuevo valor para B: "))
            continue
        print(f"{a} // {b} = {round(division_ent(a, b), 2)}")
    elif(x == 6):
        print(f"{a} ** {b} = {round(potencia(a, b), 2)}")
    elif(x == 7):
        a = float(input("Ingrese nuevo valor para A: "))
        b = float(input("Ingrese nuevo valor para B: "))
    else:
        print("VALOR INGRESADO INCORRECTO")
    print("///////////////////////////////////////////////////")

print("\n\nFIN EJECUCION PROGRAMA")

