# desafio 4
# https://sites.google.com/view/nivel1-desafios/repetitivas#h.wyfyowo1btf0

while(True):
    bandera = True  # bandera para 'pintar' el tablero con colores que
                    # alternan entre V (verde) y A (amarillo)

    x = input("Presionar ENTER para iniciar programa. "
        "Presionar 'N' y luego ENTER para salir.\n\t").upper()
    if (x == "N"):
        print()
        break
    i = int(input("Especificar el numero de filas del tablero: "))
    j = int(input("Especificar el numero de columnas del tablero: "))
    print(j*"___")
    for a in range(i): #Nota: Las filas se 'dibujan' primero.
        for b in range(j):
            if bandera:
                if (b%2 == 0):
                    print("|V|", end="")
                else:
                    print("|A|", end="")
            elif (not bandera):
                if (b%2 == 0):
                    print("|A|", end="")
                else:
                    print("|V|", end="")
        bandera = not bandera
        print()
    print()         
    print(j*"---")


print("FIN EJECUCION PROGRAMA")