# https://sites.google.com/view/complementarios/listas-tuplas-diccionarios
# Haz un programa que almacene 5 elementos en una variable del tipo
#  lista, la modiﬁque para que cada componente sea igual al cuadrado
#  del componente original. El programa mostrara la lista resultante
#  por pantalla.

# OPCION A
list_ = [1, 2, 3, 4, 5]
print(f"Lista inicial:\t\t{list_}")
i = 0
for element in list_:
    list_[i] = element**2
    i += 1
print(f"Lista modificada:\t{list_}")

# OPCION B
list_2 = [1, 2, 3, 4, 5]
print(f"Lista inicial:\t\t{list_2}")
list_2 = [x**2 for x in list_2]
print(f"Lista modificada:\t{list_2}")