# Escriba una función que tome las longitudes de los dos lados más
#  cortos de un triángulo rectángulo como sus parámetros y devuelva
#  la hipotenusa del triángulo, calculada usando el teorema de
#  Pitágoras, como resultado de la función. Incluya un programa
#  principal que lea las longitudes de los lados más cortos de
#  un triángulo rectángulo del usuario, use su función para calcular
#  la longitud de la hipotenusa y muestre el resultado.
print("Programa que calcula hipotenusa a partir de 2 lados")

from math import sqrt

def hipotenusa(x1,x2):
    x3 = sqrt((x1**2)+(x2**2))
    return x3

xA = float(input("Ingrese lado1: "))
xB = float(input("Ingrese lado2: "))

xC = hipotenusa(xA, xB)
print("La hipotenusa de ese triangulo rectangulo vale", xC)

