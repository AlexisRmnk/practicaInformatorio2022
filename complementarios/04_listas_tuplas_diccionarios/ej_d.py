# Realice una función que dada una lista de enteros L, y un número
#  entero n. Elimine de la lista original los elementos que sean
#  iguales a ese número dado.


import random
print("Lista generada de forma aleatoria:")
list_ = [random.randint(-4,4) for x in range(15)]
# forma completa abajo en comentarios

# list_ = list()
# for x in range(15):
#     list_.append(random.randint(-4,4))
print(list_)
num_ = int(input("Escribir numero entero a quitar:\n\t"))
list_ = [x for x in list_ if x != num_ ]
print(f"Lista sin el numero '{num_}':\n{list_}")


