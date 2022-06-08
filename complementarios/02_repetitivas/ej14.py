# Una pizzería, vende sus pizzas en tres tamaños: pequeña, mediana;
#  y grandes. Una pizza puede ser sencilla (con sólo salsa y carne),
#  o con ingredientes extras, tales como pepinillos, champiñones o
#  cebollas. Desarrolle una solución que calcule el precio de venta
#  de una pizza, dándole el tamaño y el número de ingredientes extras.
#  El precio de venta será 1.5 veces el costo total, que viene determinado
#  por el tamaño, más el número de ingredientes. En particular el costo
#  total se calcula sumando:

# - un costo fijo de preparación.

# - un costo variable que es proporcional al tamaño de la pizza.

# - un costo adicional por cada ingrediente extra (por simplicidad
#   se supone que cada ingrediente extra tiene el mismo costo).


# Costos "variables"
pizza_chica = 10
pizza_mediana = 18
pizza_grande = 25

costo_ingrediente = 4.5
costo_fijo = 15.5

contador = 1
while(True):
    x = input(f"Presione ENTER para calcular el precio de la pizza {contador}."
                " Presionar 'N' y luego ENTER para salir.\n\t").upper()
    if (x == "N"):
        print()
        break

    print("Ingrese el tamaño de la pizza:\n\t'C' para tamaño CHICA,"
            " 'M' para tamaño MEDIANA, 'G' para tamaño GRANDE.\n\t")
    tamanio = input().upper()
    if tamanio == "C":
        costo_variable = pizza_chica
    elif tamanio == "M":
        costo_variable = pizza_mediana
    elif tamanio == "G":
        costo_variable = pizza_grande
    else:
        print("ERROR, TAMAÑO INVALIDO - REINTENTAR\n\n")  
        continue  
    
    print("Ingrese el numero de ingredientes extras: ")
    ingredientes = int(input())
    total = costo_fijo + costo_variable + costo_ingrediente * ingredientes
    print(f"El costo de la pizza {contador} es ${round(total, 2)}")
    contador += 1

print("\nFinalizado ejecucion del programa.")


    
