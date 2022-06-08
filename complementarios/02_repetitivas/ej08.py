# Diseñar un programa que permita calcular el total de una compra,
# ingresando cantidad y precio de los productos. El programa debe
# estar preparado para que el ingreso de los datos se produzca 
# hasta que el usuario lo desee.

total = 0
producto = 1
while(True):
    x = input(f"Ingrese datos del producto {producto} - Envie 0 para salir: ")
    if (x == "0"):
        producto = producto - 1
        break

    cant = int(input("Ingrese la cantidad:\n"))
    precio = float(input("Ingrese el precio:\n$ "))
    total = total + (precio * cant)
    producto += 1

if producto == 1: # solo para mejorar el mensaje del final
    print(f"El total de la compra de 1 producto"
        f" es: ${round(total, 2)}")
else:
    print(f"El total de la compra de {producto} productos"
        f" es: ${round(total, 2)}")