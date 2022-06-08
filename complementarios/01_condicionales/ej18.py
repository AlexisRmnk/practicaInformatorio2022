# Se leen tres números que son las longitudes de los lados de un 
# triángulo. Determinar e informar si el mismo es equilátero (3 
# lados iguales), isósceles (2 lados iguales) o escaleno (3 lados
# distintos).

lado1 = float(input("Ingrese lado 1 del triangulo en cm:\n"))
lado2 = float(input("Ingrese lado 2 del triangulo en cm:\n"))
lado3 = float(input("Ingrese lado 3 del triangulo en cm:\n"))

if (lado1 == lado2 == lado3):
    print("Triangulo equilatero")
elif(lado1 != lado2 != lado3):
    print("Triangulo escaleno")
else: # (2 lados iguales y 1 distinto)
    print("Triangulo isosceles")
