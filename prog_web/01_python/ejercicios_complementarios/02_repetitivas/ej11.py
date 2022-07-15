# Hacer un programa que permita determinar todos los divisores de un
# número ingresado por el teclado.

resultado = ""
iteracion = 1

while(True):
    numero = int(input(f"ITERACION {iteracion} --- Ingrese un numero entero:\t"
                        "(envie 0 para salir)\n"))
    if (numero == 0):
        iteracion = iteracion - 1
        break
    
    print(f"\nDIVISORES DEL NUMERO {numero}: ", end="")
    for i in range(1, numero+1, 1):
        if (numero % i == 0):
            resultado = resultado + str(i) + "  "
    print(resultado)
    resultado = ""
    iteracion += 1