# Ejercicio 19: Reducir una fracción a los términos más bajos
# Escriba una función que tome dos enteros positivos que representan el
#  numerador y el denominador de una fracción como sus dos únicos parámetros.

#  El cuerpo de la función debe reducir la fracción a los términos más bajos
#  y luego devolver el numerador y el denominador de la fracción reducida
#  como resultado. Por ejemplo, si los parámetros pasados ​​a la función son
#  6 y 63, las funciones deberían volver 2 y 21. Incluya un programa
#  principal que permita al usuario ingresar un numerador y un denominador.
#  Entonces su programa debería mostrar la fracción reducida..

from def_ej_19 import *



while(True):
    print("Ingrese numerador (0 para salir)")
    num = int(input("\t"))
    if num == 0:
        print("Saliendo de programa")
        break
    print("Ingrese denominador (Cualquier entero excepto 0)")
    denom = int(input("\t"))
    if denom == 0:
        print("Valor incorrecto. Reintentar")
        continue

    fraction_positive =  is_positive(num, denom)
    num_s, den_s, already_simplified = simplify_fraction(abs(num), abs(denom))
    if not fraction_positive:
        num_s = - num_s
    if already_simplified:
        print(f"La fraccion {num}/{denom} ya se encuentra simplificada.")
    else:
        if den_s == 1:
            print(f"La fraccion {num}/{denom} simplificada es el entero"
                    f" {num_s}.")
        else:
            print(f"La fraccion {num}/{denom} simplificada es: "
                    f"{num_s}/{den_s}")


