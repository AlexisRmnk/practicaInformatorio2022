# Crea una tupla con los factores que más afectan a los mares. Luego para
#  jugar con niños y niñas, aprendiendo sobre contaminación del agua crea
#  un programa que pida números, si el numero esta entre 1 y la longitud
#  máxima de la tupla, muestra el contenido de esa posición sino muestra
#  un mensaje de error.

# El programa termina cuando el usuario introduce un cero..

tuple_factors = ("la contaminacion de las aguas con plasticos",
                "el aumento del calentamiento global",
                "las aguas residuales",
                "las sustancias químicas tóxicas",
                "las aguas pluviales"
                )

while(True):
    print(f"Seleccione un numero entre 1 y {len(tuple_factors)}:"
            "(\"0\" para salir)")
    x = int(input("\t"))
    if x == 0:
        print("PROGRAMA FINALIZADO")
        break
    elif x > len(tuple_factors) or x < 0:
        print(f"UPS! Se indico el valor {x}! este valor es invalido"
                " (es mayor al maximo permitido o es negativo)")
        print("Reintentar!")
        continue

    print(f"Sabias que uno de los factores que mas afecta a los mares es"
            f" {tuple_factors[x-1]}?")