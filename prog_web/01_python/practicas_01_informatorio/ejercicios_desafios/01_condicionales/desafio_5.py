# https://sites.google.com/view/nivel1-desafios/condicionales#h.rbj9o29toy9p
# desafio 5

nombre = input("Ingresar nombre del barrio: ")
ubicacion_num = int(input("Ingresar ubicacion del barrio: \n\t(1) si el "
                    f"barrio se encuentra ubicado en el centro.\n\t"
                    f"(2) si el barrio no esta ubicado en el centro.\n"))
nombre = nombre.upper()
if ((nombre < "M" and ubicacion_num == 1) or (nombre >= "M" and
    ubicacion_num == 2)):
    seccion = "A"
else:
    seccion = "B"

if ubicacion_num == 1:
    ubicacion = "zona centrica"
else:
    ubicacion = "zona no centrica"

print(f"El barrio {nombre.capitalize()} ubicado en {ubicacion} pertenece "
    f"a la seccion {seccion}")