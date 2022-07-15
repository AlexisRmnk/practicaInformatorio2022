# Mostrar los perímetros de varios triángulos ingresados sus lados por
# teclado, hasta que ya no desee.
i = 1

while(True):
    ciclo = input(f"Ingrese los datos del triangulo {i}: "
                    "(envie 0 para salir)")
    if (ciclo == "0"):
        i = i - 1
        break
    x1 = float(input("Ingrese longitud del lado 1 del triangulo:\n"))
    x2 = float(input("Ingrese longitud del lado 2 del triangulo:\n"))
    x3 = float(input("Ingrese longitud del lado 3 del triangulo:\n"))

    perimetro = x1 + x2 + x3
    print(f"El perimetro del triangulo {i} es: {perimetro} \n\n")