# 5) reduce (acumulador)
# A diferencia de map (que devuelve una lista), reduce toma una lista y la colapsa en un solo valor.
'Nota: hay que importarla'
# Funciona tomando los dos primeros elementos, aplicando la lambda, tomando el resultado y el siguiente elemento, y así sucesivamente. (Como una bola de nieve).
# Objetivo: Multiplicar todos los números de una lista.

from functools import reduce

numeros = [1, 2, 3, 4]

# La lambda aquí NECESITA dos argumentos: 
# x: el acumulado hasta ahora
# y: el nuevo número de la lista
producto_total = reduce(lambda x, y: x * y, numeros)

print(producto_total)
# Resultado: 24 (1*2 = 2 -> 2*3 = 6 -> 6*4 = 24)

# 5.1) REDUCE . Un concepto avanzado: El "Initialzer" (El tercer argumento)
# reduce tiene un tercer argumento opcional secreto: el valor inicial. Si lo usas, reduce no empieza con los dos primeros elementos de la lista, sino con tu valor inicial y el primer elemento.
# Ejemplo: Tienes 100 dólares en el banco y quieres sumar tus depósitos.

depositos = [20, 50, 10]
# Sin initializer empieza en 20 + 50...
# Con initializer (100), empieza calculando 100 + 20...
total = reduce(lambda saldo, ingreso: saldo + ingreso, depositos, 100)
print(total) # 180 (100 inicial + 20 + 50 + 10)
