# camel_case para Clases - MAYUSCULAS para constantes - snake_case para todo lo demas

#guardar dato de entrada teclado en variable
nombre = input("INGRESE SU NOMBRE: ")

# MOSTRAR MENSAJE POR PANTALLA, 2 formas
print("Su nombre es", nombre, " y tiene", len(nombre), "caracteres.")
print(f"Su nombre es {nombre} y tiene {len(nombre)} caracteres.")

#iniciar varias variables con un unico valor
var1 = var2 = var3 = 10

#operadores aritmeticos + - * / // % **
potencia_cuadrada = 5 ** 2 # resultado 25
division_real = 19/3 # da de resultado 6.33 periodico
division_entera = 19//3 # da de resultado 6
modulo_division = 19 % 3 # da de resultado el resto de hacer 19/3, es decir "1"

# operadores de comparacion > >= < <= == !=
# operadores logicos AND OR NOT XOR
# operadores CON CADENAS * y +

# podemos corroborar el tipo de una variable con el comando type(variable)
entero = 10
print(type(entero))

# tipos de variables: 
# conjunto - NO TIENE ELEMENTOS QUE SE REPITEN
conjunto_tipo_set = {"test", 1, True, 2.5, "a"}

#lista
lista_1 = ["elemento_0", "elemento_1", entero, True]    # tiene indices del
                                                        # 0 en adelante
elemento_1 = lista_1[1]

#tupla
tupla = ("alpha", "beta", 1, True) #como una lista pero NO modificable

# diccionario - trabajan con LLAVES en vez de indices
diccionarioTest = {
    "Y": "ypsilon" ,
    "cadena": "valor cadena",
    True: "valor true",
    False: "valor false",
    1: "uno",
    "dos": 2
}
print("Nuestro diccionario es de tipo: ", type(diccionarioTest), 
", visto con el comando type(variable)")
print('diccionarioTest["Y"]', diccionarioTest["Y"])
print('diccionarioTest["cadena"]', diccionarioTest["cadena"])
print('diccionarioTest[True]', diccionarioTest[True])
print('diccionarioTest[False]', diccionarioTest[False])
print('diccionarioTest[1]', diccionarioTest[1])
print('diccionarioTest["dos"]', diccionarioTest["dos"])

# Python incorpora un quinto tipo de dato que estrictamente hablando 
# se llama ​NoneType ​y cuyo único valor posible es None.

#conversion de tipos/CASTING 
cadena = "10"
caracter = "a"
entero = 10
flotante = 10.5
booleano = True

cadena_convertido_a_entero = int(cadena) 
cadena_convertido_a_decimal = float(cadena)
entero_convertido_a_cadena = str(entero)
entero_convertido_a_cadena_hexadecimal = hex(entero) #tipo str
entero_convertido_a_caracter = chr(entero) #tipo str
caracter_convertido_a_entero = ord(caracter)
cadena_convertido_en_numero_complejo = complex("10+5j")
#caso bool(): el 0 y el None lo convierte en "False". 
# El resto en "True".
booleano_True = bool("Cualquier cosa")
booleano_False = bool(0); 
booleano_False2 = bool(None); 
# podemos corroborar el tipo de una variable con el comando type(variable)
print(type(entero))

# ESTRUCTURAS DE CONTROL
# CONDICIONALES
# Condicional Simple: sentencia IF
condicion_verdadera = True
if (condicion_verdadera):
    print("SI")

if (condicion_verdadera):
    if (condicion_verdadera):
        print("SI")

# Condicional alternativo o doble: sentencia ELSE
condicion_falsa = False

if (condicion_falsa):
    print("...")
else:
    print("SI")

# Condicional multiple: sentencia ELIF

if (condicion_falsa):
    print("...")
elif(condicion_falsa):
    print("...")
elif(condicion_falsa):
    print("...")
elif(condicion_verdadera):
    print("SI")
elif(condicion_falsa):
    print("...")

# REPETITIVAS
# Cada conjunto de instrucciones a ejecutar se denomina BUCLE.
#  Y cada repetición del bucle se llama ITERACIÓN
# Se usan CONTADORES, ACUMULADORES y BANDERAS

# Sentencia WHILE
cont = 0
suma = 0
n = int(input('Ingrese tope maximo: '))
while (cont <= n):
    suma = suma + cont
    cont = cont + 1
print('La suma total es: ', suma)

# --

numero = int(input("Escriba un numero positivo: "))
while numero < 0:
    print("Ha escrito un numero negativo. Intentelo de nuevo.")
    numero = int(input("Escriba un numero positivo: "))
print("bien hecho")

# while con else
# Se encadena al While para ejecutar un bloque de código una vez la 
# condición ya no devuelve True (normalmente al final):

c = 0
while c <= 2:
    c+=1 
    print("c vale", c) #imprime c=1, c=2, c=3
else:
    print(f"Se ha completado toda la iteracion y c vale {c}") #imprime c=3

# sentencia FOR
lista_auxiliar = ["a", "b", 1, 2, 3]
i = 0 #contador auxiliar
for elemento in lista_auxiliar:
    print(f"El elemento numero {i} de la lista es {elemento}") #{lista_auxiliar[i]}")
    i+=1
print("Fin FOR")

    # for con tipos "range()"
for i in range(5):
    print(f"i = {i} ", end="")

# instruccion/sentencia break
# Se puede usar en bucles ​for ​y ​while ​y 
# simplemente t​ermina el bucle actual

# Uso 1: controlar fin de bucle
while True:
    x = input("Ingrese cualquier palabra, termina con FIN --->")
    if x == "FIN":
        break
    else:
        print(x)
print("Salimos del bucle WHILE escribiendo FIN")

# La sentencia break es usada también para terminar un ciclo aun cuando
# la evaluación de la condición no devuelva False

for letra in "abcdefghijklmno":
    if letra == "f":
        break
    print("Letra actual :", letra)

var = 10
while var > 0:
    var = var -1
    if var == 5:
        break
    print("Valor actual de la variable :", var)

# Sentencia continue
# Al aparecer un ​continue ​en Python, este regresa al comienzo del bucle,
# ignorando todos los estamentos que quedan en la iteración actual del
# bucle e inicia la siguiente iteración. 

for letra in "Python":
    if letra == "h":    
        continue
    print("Letra actual :", letra)

var = 10
while var > 0:
    var = var -1
    if var == 5:
        continue
    print("Valor actual de la variable :", var)



## FUNCIONES

def funcion():
    '''Funcion sin parametros y sin retorno'''
    print("xd")

def funcion1():
    '''Funcion sin parametros y con retorno'''
    return "ValorFuncion1"

def funcion2(parametro1, parametro2):
    '''Funcion con parametros y con retorno'''
    suma = parametro1 + parametro2
    return ("Valor funcion2: " +  str(suma))

#ej llamada a funcion
x = funcion1()
print(x)

argumento1 = 1
argumento2 = 2
x = funcion2(argumento1, argumento2)
print(x)


def funcion3 (parametro1 = 1, parametro2 = 2, parametro3 = 3):
    '''funcion con VALORES POR DEFECTO'''
    # los parametros tienen valores por defecto en caso de que no se asignen
    return parametro1 + parametro2 + parametro3
print(f"Suma de  1,   2  y   3 :  {funcion3()}")
print(f"Suma de *5*,  2  y   3 : {funcion3(5)}")
print(f"Suma de *5*, *7* y   3 : {funcion3(5, 7)}")
print(f"Suma de *5*, *7* y *13*: {funcion3(5, 7, 13)}")

# que pasa si el valor opcional es el primero? el de mas a la izq
# PONER LOS VALORES 'POR DEFECTO' AL FINAL! 
def funcion5 (parametro2, parametro3, parametro1 = 1):
    '''funcion con VALORES POR DEFECTO'''
    # los parametros tienen valores por defecto en caso de que no se asignen
    return parametro1 + parametro2 + parametro3

print(f"Suma de 5, *7* y *13*: {funcion5(parametro2 = 7, parametro3 = 13)}")


#devolver mas de 1 valor en una funcion! sin listas ni nada
def funcion4(x):
    '''funcion que suma a si mismo un valor y tambien lo multiplica'''
    respuesta1 = x + x
    respuesta2 = x * x
    return respuesta1, respuesta2
x = 3
r1, r2 = funcion4(x)
print(f"{x} + {x} = {r1}")
print(f"{x} * {x} = {r2}")




# importar funciones/procedimientos 
# [Este codigo se escribe en el .py principal]
# from ARCHIVO import nombre_funcion
from archivo_funciones import nombre_funcion1, nombre_funcion2

# [Este codigo se escribe en el .py de funciones]
if __name__ == '__main__':
    print("HOLA") # estas lineas codigo solo se van a ejecutar si se 
    # ejecuta la funcion desde la terminal

import archivo_funciones #trae todo el progama como un objeto!
# se usan las funciones escribiendo: 
archivo_funciones.nombre_funcion1

# para importar TODAS las funciones, se usa
from archivo_funciones import *

# ejemplo en    [practicas_varias\importarPracticas\principal.py]
#               [practicas_varias\importarPracticas\funciones_1.py]



# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# *Set items are unchangeable, but you can remove items and add new items.
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# set 
set_ = {1, 2, 3, 4} 


# listas
# crear vacia
lista_nueva = list()
lista_nueva2 = []

# crear con elementos
lista_nueva3 = ["a", 1, True]
lista_larga = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 
1, 1, 0, 5, 4, 7, 8 ]

# añadir elemento
elemento = True
lista_nueva.append(elemento)
lista_nueva.append(3); lista_nueva.append(4); lista_nueva.append(-1)
lista_nueva.append(11); lista_nueva.append(0); lista_nueva.append(3)

lista_nueva.insert(elemento, 2) # agrega elemento en la posicion 2

# modificar elemento
lista_nueva[1] = 99

# ordenar lista
lista_nueva.sort()
# en sentido inverso
lista_nueva.sort(reverse = True)

# invertir lista
lista_nueva.reverse()

# longitud de lista
x = len(lista_nueva)

# saber elemento en posicion particular
x = lista_nueva[1]
# lo mismo pero viendo de atras hacia adelante (<--)
x = lista_nueva[-1]

# recorrer lista
for x in lista_nueva:
    print(f"Elemento: {x}")

# extender lista 
lista_nueva.extend(lista_larga)

# crear sublistas  (slicing)
# crea una lista nueva con los elementos 2, 3 y 4 de otra lista
lista_nueva4 = lista_nueva[2:5] #tambien se usa [:2] [2:] [:] 

# listas anidadas
lista_z = [1, ["a", "b", "c"], 3, 4]
lista_y = [[1, 2, 3], [4, 5, 6]]
for y in lista_y:
    prom = sum(y)/len(y)
    print(f"El promedio de cada elemento de lista es: {prom}")

# copiar lista
copia_lista = lista_nueva[:]
copia_lista_v2 = lista_nueva.copy()

# como NO copiar una lista:
# lo siguiente NO CREA UNA LISTA NUEVA, sino que crea UN NUEVO APUNTADOR
# A UNA MISMA LISTA! (hace pasaje por referencia) ej:
lista_x = [1, 2, 3]
lista_y = lista_x # esto NO copia una lista
lista_y.append(99)
print(lista_x) #imprime [1, 2, 3, 99] !

# modificar varios elementos de una lista a la vez
colores = ["rojo","verde","azul","rosado"]
colores[1:3] = ["amarillo", "violeta"]
print(colores) # ["rojo","amarillo","violeta","rosado"]

# saber si elemento esta en lista usando IN
if 3 in lista_nueva:
    print("El 3 esta en la lista")
# Saber cuantas veces se encuentra un elemento dentro de una lista 
print(f"El 3 aparece {lista_nueva.count(3)} veces en la lista")
# conocer indice de elemento(solo devuelve la primer coincidencia!)
print(lista_nueva.index(3))

#eliminar elemento (por indice con DEL y por elmento con REMOVE)
del lista_nueva[0]
del lista_nueva[1:4] # borra elementos del indice 1 al 3 incluido (4 sin incluir)
lista_nueva.remove(99) #borra el elemento "99". SOLO LA PRIMERA COINCIDENCIA!
lista_nueva_ultimo_elemento = lista_nueva.pop()
lista_nueva_segundo_elemento = lista_nueva.pop(1)

#funciones de listas varias
# sum() len() max() min()
# se pueden usar operadores matematicos en listas!
# resultado = una_lista + otra_lista


# LIST COMPREHESION
# permite creare listas a partir de iterables usando la siguiente estructura:
#   [ expression for elemento in iterable if condicion ]

#   una lista con los triples de estos numeros:
numeros = [3, 8, 1, 9]
triples = [x*3 for x in numeros] # "por cada X en numeros, agregame un x*3 en triples"

# ej: todos los números pares desde el 0 al 100
pares = [x for x in range(0,101) if x %2 == 0]

# ej: todos los cuadrados de los números pares (del 0 al 100)
pares_cuadrado = [x**2 for x in range(0,101) if x %2 == 0]


#TUPLAS
# son como listas, pero INMUTABLES. Se indican entre parentesis
tupla_nueva = tuple()
tupla_nueva = ()
tupla_nueva = (3,)
# metodos count() index() max() min() sum() len()

# se pueden empaquetar y desempaquetar tuplas.




# DICCIONARIOS
# crear
diccionario = {}
diccionario2 = dict()
diccionario3 =  { "key1":"value1",
                    "key2":"value2"
                }

# agregar elemento
diccionario['clave'] = "valor"
diccionario['key'] = "value"

# actualizar/modificar valor
diccionario['clave'] = "valor_actualizado" 

# acceder a valor en clave "key"
valor_de_clave_key = diccionario["key"]
# para evitar errores, se usa metodo get
valor_de_clave_key = diccionario.get("key")
# si no encuentra nada, devuelve None
# se puede configurar la devolucion por defecto en caso de no existir "key"
valor_de_clave_key = diccionario.get("key", "no existe \"key\" ")
print(valor_de_clave_key)


#setDefault para agregar valor solo si no existia antes!
diccionario.setdefault("ClaveNueva", "ValorNuevo")

# imprimir valores
print(diccionario.values())

#   imprimir claves
print(diccionario.keys())

# recorrer diccionario:
# por clave.
for key in diccionario:
    print(f"clave --> {key}, valor ---> {diccionario[key]}")

# imprimir LISTA de TUPLAS "Key, Value"
for clave, valor in diccionario.items():
    print(f"clave --> {clave}, valor ---> {valor}")
# diccionario.items() devuelve una LISTA DE TUPLAS.
# el "for" recorre cada elemento (que es una tupla clave,valor)
#  y la va imprimiendo con el print

# verificar si una clave se encuentra en el diccionario
if ("clave" in diccionario):
    print(f'La clave "clave" se encuentra en el diccionario y su elemento es '
        f'{diccionario["clave"]}')

# eliminar clave:valor
del diccionario["clave"]
valor = diccionario.pop("clave") #si no existe la clave devuelve ERROR
# por ello podemos usar mejor un mensaje predeterminado por si no existe clave
valor = diccionario.pop("clave", "No existe la clave 'clave' ")

# vaciar diccionario
diccionario.clear()

# EXTENDER o ACTUALIZAR diccionario con UPDATE()
diccionario1 = {"a":1, "b":2, "c":3}
diccionario2 = {"c":30, "d":40, "e":50}
print(diccionario1, diccionario2)
diccionario1.update(diccionario2)
print(diccionario1) # {'a': 1, 'b': 2, 'c': 30, 'd': 40, 'e': 50}

# Funciones y metodos
d = diccionario1.copy()
x1 = d.keys(); x2 = d.values(); x3 = d.items(); x4 = len(d)
# es importante destacar x1, x2 y x3
# estos metodos generan VISTAS. Es decir, si modificamos el 
# diccionario 'd', las vistas reflejaran dichos cambios!
# para guardar los valores en un momento dado se puede usar list() o tuple()
# ej:
print(x1) # dict_keys(['a', 'b', 'c'])
print(x2) # dict_values([1, 2, 3])
print(x3) # dict_items([('a', 1), ('b', 2), ('c', 3)])
print(x4) # 3 (NO ES UNA VISTA)
d.pop("c")      # borrado elemento con key="c"
print(x1) # dict_keys(['a', 'b'])
print(x2) # dict_values([1, 2])
print(x3) # dict_items([('a', 1), ('b', 2)]))
print(x4) # sigue siendo 3 (NO ES UNA VISTA)



# Comparacion entre listas:
# cuando se comparan 2 listas, la "mayor" sera la que tenga el primer elemento
# mayor que la otra lista.
# ejs: 
[2] > [1, 2, 3] # True
[1, 2, 2] > [1, 2, 3] # False
[1] < [1, 2] # True

a = [1, 2, 3]
b = [1, 2, 3]
print(a is a) # True
b is a # False
b == a # True

