# Solicitar el ingreso de números al usuario y emitir un mensaje para 
# determinar si es par o impar. El ciclo debe finalizar cuando el 
# usuario ingresa 0.


while(True):
    x = int(input("Introduzca un numero para saber si es par o impar"
                    " (numero 0 para salir)\n"))
    if (x == 0):
        break
    elif (x % 2 == 0):
        print(f"El numero {x} es PAR")
    else:
        print(f"El numero {x} es IMPAR")

print("FIN EJECUCION")
