# Diseñar un programa que lea las longitudes de los tres lados 
# de un triángulo (L1,L2,L3) y determine qué tipo de triángulo es,
# de acuerdo a los siguientes casos. Suponiendo que A determina 
# el mayor de los tres lados y B y C corresponden con los otros dos,
# entonces:

# Si A >= B + C  No se trata de un triángulo
# Si A**2 = B**2 + C**2  Es un triángulo rectángulo
# Si A**2 > B**2 + C**2  Es un triángulo obtusángulo
# Si A**2 < B**2 + C**2  Es un triángulo acutángulo

print("Ingrese las longitudes en centimetros de los 3 lados del rectangulo.")
a = float(input("Lado A (el mas largo):\n"))
b = float(input("Lado B:\n"))
c = float(input("Lado C:\n"))


if (a > b and a > c):
    if( a >= b+c):
        print("Esto no es un triangulo.")
    else:
        if(a**2 == b**2 + c**2):
            print("Triangulo rectangulo.")
        elif (a**2 > b**2 + c**2):
            print("Triangulo obtusangulo.")
        elif (a**2 < b**2 + c**2):
            print("Triangulo acutangulo")
else:
    print("Algun dato se ingreso mal (A mide menos que B o C)")