# desafio 3
# https://sites.google.com/view/nivel1-desafios/repetitivas

print("Iniciando ejercicio. Entrando bucle While.\n")
i = j = subtotal = 0


while(True):
    i += 1
    x = input((f"Ingrese los datos de compra del cliente {i}:"
    " (Introdusca N para salir del programa / oprima "
    "cualquier otra tecla para continuar)\n \t")).upper()
    if x == "N":
        break
    
    while(True):
        j += 1
        cant = int(input(f"Ingrese la cantidad del producto {j}: "))
        precio = float(input(f"Ingrese el precio del producto {j}:  $"))
        subtotal = subtotal + (cant * precio) # acumulador
        desicion = input(f"Desea agregar mas productos? (S/N): ")
        desicion = desicion.upper()
        if desicion == "S":
            continue
        elif desicion == "N":
            j = 0
            break
        else:
            print("Se ha introducido un comando inesperado, se interpreta"
                " como respuesta afirmativa.")
    print("En caso de tener un codigo de descuento introducirlo"
    " a continuacion:")    
    desc_code = input("(Codigos: ROJO, AMARILLO, BLANCO)").upper()
    if desc_code == "ROJO":
        desc_porcentaje = 0.4
    elif desc_code == "AMARILLO":
        desc_porcentaje = 0.25
    else:
        desc_porcentaje = 0

    total = subtotal - subtotal * desc_porcentaje
    print(f"CLIENTE {i}:\t SUBTOTAL: ${round(subtotal, 2)}")
    print(f"\t\t - DESCUENTO: ${round(subtotal*desc_porcentaje,2)}")
    print("__________________________________________")
    print(f"\t\t TOTAL: ${round(total, 2)}")
    j = 0
    subtotal = 0

    print("******************************************************************")
    
print("FIN EJECUCION")