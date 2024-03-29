# continuacion del apunte gral en 
# \practicas_02_adicional_informatorio\practicas_varias\999_apuntes_varios.py

# nuevo (11-01-23 en adelante)
# estudiando de libro "El gran libro de python (Marco Buttu)"
# una variable es solo una etiqueta mediante la cual se representa un objeto especifico
# por ej: todos estos prints de id de objeto devuelven la misma secuencia

lista = [1, True, 3]
item = lista[0]
print(id(item)) # 2472082800880
item = lista[1]
print(id(item)) # 140711200336744
item = lista[2]
print(id(item)) # 2472082800944 

print("")
print(id(lista[0])) # 2472082800880
print(id(lista[1])) # 140711200336744
print(id(lista[2])) # 2472082800944

print("")
print(id(1)) # 2472082800880
print(id(True)) # 140711200336744
print(id(3)) # 2472082800944



# detalle: de -5 a 256 el valor de id no cambia en sus re-ejecucioens
a = id(1)
b = id(2)
c = id(256)
print('no cambian:',a, b, c, sep='\n')

a = id(257)
b = id(258)
c = id(259)
print('si cambian:',a, b, c, sep='\n')



# saber los atributos de un objeto cualquiera con dir
# por ej: objeto iterable range
r = range(3, 30, 4)
print('type(r):', type(r) ) # >    <class 'range'>
print('dir(r):', dir(r) ) # >    ['__bool__', ... , 'count', 'index', 'start', 'step', 'stop']
print( 'hasattr(r, "start"):', hasattr(r, "start") , '| r.start: ', r.start )
    # > hasattr(r, "start"): True | r.start:  3

# Expresiones logicas OR y AND
# usando OR y AND puedo devolver resultados de forma similar a con JS 
#                          cuando usabamos operadores de cortocircuito

t = [1, [2,3], True] 
f = [0 , {}, False]

# OR logico devuelve primer obj Verdadero 
print((f[0] or f[1] or t[0] or t[1] or f[2])) 
    # imprime 1 (primer objeto verdadero correpondiente a t[0])

# AND logico devuelve primer obj falso
print((t[0] and t[1] and f[0] and f[1] and t[2]))
    # imprime 0 (primer objeto falso correpondiente a f[0])
    

# DESEMPAQUETADO
# se pueden desempaquetar los objetos iterables
a, b, c = [1, 2, 3]
print(a, b, c)

a, b, c = "hey"
print(a, b, c)

# se puede desempaquetar unicamente cuando las etiquetas a la izquierda de la asignacion estan dentro de una lista o tupla. 
# Para indicar una lista de un solo elemento se puede usar la siguiente notacion:
[a] = [1]
print(a) # 1
print(type(a)) # int

#es distinto a, por ejemplo hacer:
a = [1]
print(a) # 1
print(type(a)) # list <-- diferencia

# Para indicar una tupla de un solo elemento se puede usar la siguiente notacion
b, = [2]
print(b) # 2
print(type(b)) # int


# DESEMPAQUETADO EXTENDIDO
# basicamente sirve para indicar que se recibira una lista de valores, se puede ocupar en cualquier parte del desempaquetado. EJ:
*a, b, c = "python"
print("a: ", a) # a:  ['p', 'y', 't', 'h'] 
print("b: ", b) # b:  o 
print("c: ", c) # c:  n 
print("") 

a2, *b2, c2 = "python"
print("a2: ", a2) # a2:  p 
print("b2: ", b2) # b2:  ['y', 't', 'h', 'o'] 
print("c2: ", c2) # c2:  n 
print("")   

a3, b3, *c3 = "python"
print("a3: ", a3) # a3:  p 
print("b3: ", b3) # b3:  y 
print("c3: ", c3) # c3:  ['t', 'h', 'o', 'n'] 
print("\n") 

# caso con IGUAL CANTIDAD de elementos en el objeto iterable (cadena en este ejemplo)
*a4, b4, c4 = "abc"
print("a4: ", a4) # a4:  ['a']
print("b4: ", b4) # b4:  b
print("c4: ", c4) # c4:  c
print("")  

a5, *b5, c5 = "abc"
print("a5: ", a5) # a5:  a
print("b5: ", b5) # b5:  ['b']
print("c5: ", c5) # c5:  c
print("") 

a6, b6, *c6 = "abc"
print("a6: ", a6) # a6:  a
print("b6: ", b6) # b6:  b
print("c6: ", c6) # c6:  ['c']
print("\n")  

# caso con MENOS elementos en el objeto iterable (cadena en este ejemplo)
*a7, b7, c7 = "de"
print("a7: ", a7) # a7:  []
print("b7: ", b7) # b7:  d
print("c7: ", c7) # c7:  e
print("") 

a8, *b8, c8 = "de"
print("a8: ", a8) # a8:  d
print("b8: ", b8) # b8:  []
print("c8: ", c8) # c8:  e
print("") 

a9, b9, *c9 = "de"
print("a9: ", a9) # a9:  d
print("b9: ", b9) # b9:  e
print("c9: ", c9) # c9:  []


# Desempaquetado con for
for *i, j in [ "gato", [1,2,3], "python", "perro" ]:
    print("i: ", i)
    print("j: ", j)
    print("")
    
# Desempaquetado con for (usando enumeracion)
for iteration,[*i, j] in enumerate([ "gato", [1,2,3], "python", "perro" ]):
    print(f"iteracion {iteration}:")
    print("i: ", i)
    print("j: ", j)
    print()
    

# 'all' y 'any' permiten determinar en un iterable si:
    # 'all': todos los objetos son True
    # 'any': hay al menos 1 obj True
    
t = [1, [2,3], True] 
f = [0 , {}, False]
tf = [1, [2,3], True, 0] #el 0 es false
print(" all(t): ", all(t))
print(" all(f): ", all(f))
print(" all(tf): ", all(tf), end="\n")

print(" any(t): ", any(t))
print(" any(f): ", any(f))
print(" any(tf): ", any(tf), end="\n")
'''
    all(t):  True
    all(f):  False
    all(tf):  False
    any(t):  True
    any(f):  False
    any(tf):  True
'''

# zip puede usarse para generar un iterador y recorrer a la vez varios objetos iterables
iterable1 = "abc"
iterable2 = [1, 2, 3]
iterable3 = (True, False, None, "(no se imprime, ver abajo nota 'A')")

z = zip(iterable1, iterable2, iterable3)
for item in z:
    print(item)
#('a', 1, True)
#('b', 2, False)
#('c', 3, None)

# nota 'A': no se imprime nada mas porque solo se itera el minimo posible


# map() sirve para ejecutar una funcion para una serie de elementos en un iterable
def def_square(x):
    return x ** x

iterable = [1, 2, 3]
m = map(def_square, iterable)
for i in m:
    print(i)
# un map puede ser iterado 1 sola vez! si intento usarlo de nuevo: 
for i in m:
    print(i) # no va a imprimir nada!
    
# para guardar valores del map en una lista
m = map(def_square, iterable) # volvemos a generar el map
lista_valores = list(m)

# se pueden usar 2 iterables si la funcion necesita mas de un parametro
def def_product(x, y):
    return (x * y)

iterable = [1, 2, 3, 4]
iterable2 = [10, 100, 1000] # al no poner un elemento mas, esto solo va a iterar 3 veces
m2 = map(def_product, iterable, iterable2)
for i in m2:
    print(i)


# filter() sirve para agarrar un iterable, hacer pasar sus elementos por una 
# funcion, y filtrar aquellos que NO sean False o un equivalente
def def_checks_even_n(x):
    return (not x%2) #devuelve True si X es par
    # nota: el not me transforma el 1 o 0 en booleano

iterable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # pude haber hecho con range(10)
f = filter( def_checks_even_n, iterable)

for item in f:
    print(item)
# al igual que con map(), solo se puede recorrer una vez
    
# tambien es posible hacer un filtro cuyo primer parametro en vez 
# de ser funcion, sea None
for i in filter(None, range(-5, 5, 1)):
    print(i)
# en este caso imprime -5  -4  -3  -2  -1  1  2  3  4
# Saltea el 0. Esto supongo que es porque el filtro lo considera FALSE directamente


# copiar un diccionario de forma correcta
dict1 = {0: "0", 1:"1", 2:"2"}
dict1_copy = dict1.copy()

print(f"dict1: {dict1} - dict1_copy: {dict1_copy}")
dict1[1] = "otra cosa"
print(f"dict1: {dict1} - dict1_copy: {dict1_copy}")


# para salir de un programa ejecutado en consola:
# exit()


#como escribir comillas en una cadena (escape characters)
cadena = " \" "; cadena = ' " '


#como leer un archivo en excel (Libreria PANDAS)
import pandas as pd
df = pd.read_excel('file.xlsx')


# como operar con decimales sin problemas
from decimal import Decimal

a = Decimal("55.2")
print(f"x1: {a / Decimal('10')}")
print(f"x2: {a // Decimal('10')}")
print(f"x3: {a % Decimal('10')}")


# uso de etiquetas de comentarios especiales en VS CODE
# TODO: para marcar algo que se debe comletar en el futuro
# FIXME: para marcar el codigo especifico que requiere arreglo
# NOTE: para anotar algo de forma resaltada
# HACK: para arreglo temporales
# XXX: para marcar codigo que se puede mejorar, documentar u optimizar
# REVIEW: (no coloreado nativamente por VS CODE) para marcar codigo que requiere revision




# test impresion paths
# funciona en Jupyter Notebook (.ipynb) Y en archivo python (.py)
import sys
print(r"IMPRIMIENDO PATH ############################################")
print(sys.path[0])
print(r"#############################################################")

# funciona solo en archivo python (.py)
import os
directorio_actual = os.path.dirname(os.path.abspath(__file__))
print(directorio_actual)