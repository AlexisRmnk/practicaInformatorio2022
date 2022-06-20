# Realiza una función llamada relacion(a, b) que a partir de toneladas
#  recicladas de dos ciudades se cumpla lo siguiente:
# Si el primer número es mayor que el segundo, debe devolver el nombre de
#  la ciudad 1.
# Si el primer número es menor que el segundo, debe devolver el nombre de
#  la ciudad 2.
# Si ambos números son iguales, debe devolver el nombre de ambas.
from def_desafio02 import relacion

print("Ingrese nombre y toneladas recicladas de la ciudad 1:")
city_1_name = input("Nombre ciudad 1:\n\t")
city_1_amount = float(input(f"Cantidad de toneladas recicladas en "
                            f"{city_1_name}\n\t"))
city_1 = (city_1_name, city_1_amount)
print("Ingrese nombre y toneladas recicladas de la ciudad 2:")
city_2_name = input("Nombre ciudad 2:\n\t")
city_2_amount = float(input(f"Cantidad de toneladas recicladas en "
                            f"{city_2_name}\n\t"))
city_2 = (city_2_name, city_2_amount)

city_bigger_amount, bool_ = relacion(city_1, city_2)
if bool_:
    print(f"{city_bigger_amount} tienen la misma cantidad de toneladas"
            " recicladas")
else:
    print(f"{city_bigger_amount} tiene mas toneladas recicladas")