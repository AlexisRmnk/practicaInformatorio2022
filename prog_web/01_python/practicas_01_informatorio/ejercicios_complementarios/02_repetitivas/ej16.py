#  Escribir un programa el cual lea dos valores enteros. 
# Si el primero es menor que el segundo, que imprima el mensaje ``Arriba''.
#  Si el segundo es menor que el primero, que imprima el mensaje ``Abajo''.
#  Si los números son iguales, que imprima el mensaje ``igual''.
#  Si alguno de los datos ingresados es igual a 0, que imprima un mensaje
#  conteniendo la palabra ``Error''.

x = int(input("Ingrese el primer numero entero:\n\t"))
y = int(input("Ingrese el segundo numero entero:\n\t"))

if (x == 0 or y == 0):
    print("ERROR")
elif (x<y):
    print("Arriba")
elif (y<x):
    print("Abajo")
elif (y == x):
    print("Igual")
