# k. 	Cargue dos listas, y actualice la primer lista con los elementos
#  que están en la segunda y no en la primera.

# notas: vamos a cargar la lista con valores aleatorios

import random
list_1 = list()
list_2 = list()

for i in range(10):
    list_1.append(random.randint(1, 10))
    list_2.append(random.randint(1, 10))

list_1.sort()
list_2.sort()
print(f"Lista 1: {list_1} \nLista 2: {list_2}")
print()

#recorremos una lista, comparamos y si no esta agregamos.
for element_ in list_2:
    if element_ not in list_1:
        print("Se agrego el elemento ", element_)
        list_1.append(element_)

list_1.sort()
print(f"Lista 1 NUEVA:\t{list_1} \nLista 2: \t{list_2}")