# Cargar dos listas con la misma cantidad de elementos. Luego mezclarlas,
#  cargándolas ordenadas en otra lista.
list_1 = [ 1,   6, 8, -1, 0, 15]
list_2 = [99, -50, 2,  0, 1, 13]
print(f"Lista 1: {list_1}")
print(f"Lista 2: {list_2}")

list_1.sort()
list_2.sort()

print(f"Lista 1 ordenada: {list_1}")
print(f"Lista 2 ordenada: {list_2}")

list_3 = list()
for j in range(len(list_1)):
    if list_1[j]<list_2[j]:
        list_3.append(list_1[j])
        list_3.append(list_2[j])
    else:
        list_3.append(list_2[j])
        list_3.append(list_1[j])

print(f"Lista 3: {list_3}")