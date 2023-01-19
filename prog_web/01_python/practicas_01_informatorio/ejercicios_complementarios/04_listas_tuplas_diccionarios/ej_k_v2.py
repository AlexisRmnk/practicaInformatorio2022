# Cargue dos listas, y actualice la primer lista con los
#  elementos que están en la segunda y no en la primera.
# version propia usando List comprehesion

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
print(f"Lista 1: {list_1}")
print(f"Lista 2: {list_2}")

list_aux = [x for x in list_2 if (x not in list_1)]
list_1.extend(list_aux)
print(f"Lista 1 actualizada con los elmentos extra de lista 2: {list_1}")
