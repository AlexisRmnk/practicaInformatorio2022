# desafio 4
# https://sites.google.com/view/nivel1-desafios/repetitivas#h.wyfyowo1btf0

# imprimir tablero 8x6

while(True):
    x = input("Presionar cualquier tecla para iniciar programa. "
        "Presionar 'N' para salir.\n\t").upper()
    if (x == "N"):
        print()
        break
    i = int(input("Especificar el numero de filas del tablero: "))
    j = int(input("Especificar el numero de columnas del tablero: "))
    print(j*"___")
    for a in range(i): #Nota: Las filas se 'dibujan' primero.
        for b in range(j):
            print("|_|", end="")
        print() 
    print("")                       
    print(j*"---")


print("FIN EJECUCION PROGRAMA")