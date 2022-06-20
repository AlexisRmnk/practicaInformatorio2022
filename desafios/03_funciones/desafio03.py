# Realiza una función separar(lista) que tome una lista que tenga datos
#  de cantidad de árboles plantados en diferentes ciudades de Argentina
#  durante la cuarentena. Luego la función debe devolver dos listas
#  ordenadas. La primera con las cantidades que superen los 100 y la
#  segunda con el resto.
from def_desafio03 import separar

list_cities = list()
i = 0
print("Ingrese la cantidad de arboles plantados en las distintas "
        "ciudades argentinas durante la cuarentena del 2021-2022.")
while(True):
    i += 1
    print(f"Ingrese nombre de ciudad {i}:")
    name_ = input("\t").capitalize()
    print(f"Ingrese cantidad de arboles plantados en {name_}:")
    quantity = int(input("\t"))
    list_cities.append((name_, quantity))

    print("Apretar ENTER para ingresar otra ciudad (0 para salir).")
    x = input("\t")
    if x == "0":
        break

cities_more_100, cities_less_or_100 = separar(list_cities)

print(f"Ciudades con mas de 100 arboles plantados:")
for city_, quantity in cities_more_100:
    print(f"En {city_} se plantaron {quantity} arboles.")

print(f"\nCiudades con menos de 100 o 100 arboles plantados: ")
for city_, quantity in cities_less_or_100:
    print(f"En {city_} se plantaron {quantity} arboles.")