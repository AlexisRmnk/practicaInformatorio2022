# Elabore un programa que dada una lista de 15 elementos,
#  copie en otra lista los elementos pares multiplicados por 2.

list_1 = [1, 10, 100, 0, -1, -10, -100, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Lista_1 con 15 elementos:\t\t{list_1}")

list_2 = [x*2 for x in list_1 if x%2==0]

print(f"Lista de elementos pares de Lista_1, multiplicados por 2:{list_2}")