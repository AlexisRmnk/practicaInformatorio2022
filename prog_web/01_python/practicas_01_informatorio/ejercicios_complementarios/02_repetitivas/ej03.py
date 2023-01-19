# Diseñar un programa que permita obtener el producto entre A y B
# mediante sumas sucesivas.

x = int(input("Ingrese un numero entero x:\n"))
y = int(input("Ingrese un numero entero y:\n"))

acumulador = 0
for i in range(y):
    acumulador = acumulador + x

print("x * y =", acumulador)

