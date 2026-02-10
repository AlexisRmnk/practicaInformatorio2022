# Anotaciones varias. 
# CamelCase para Clases - MAYUSCULAS para constantes - snake_case para todo lo demas

#guardar dato de entrada teclado en variable
nombre = input("INGRESE SU NOMBRE: ")

# MOSTRAR MENSAJE POR PANTALLA, 2 formas
print("Su nombre es", nombre, "y tiene", len(nombre), "caracteres.")
print(f"Su nombre es {nombre} y tiene {len(nombre)} caracteres.")

# probando con format, funcion de 'string'
txt_format = 'Su nombre es {nombre_0} y tiene {long:.2f} caracteres.'
print(txt_format.format(nombre_0 = nombre, long = len(nombre)))


#iniciar varias variables con un unico valor
var1 = var2 = var3 = 10
#iniciar varias variables con distintos valores (usando desempaquetado)
var1v2, var2v2, var3v2 = 10, 20, 30

#guardar texto largo
str_largo_1 = '''
This is a long string
that spans multiple lines.
It can contain any characters,
including special characters
and line breaks. '''

str_largo_2 = """
This is a long string
that spans multiple lines.
It can contain any characters,
including special characters
and line breaks. """

# Usando secuencias de escape (escape sequences) - no tiene saltos de linea
str_largo_3 = "This is a long string \
that spans multiple lines. \
It can contain any characters, \
including special characters \
and line breaks."

# ejemplo de escape sequences en un comando
x_escape_seq = 1 + 1 + 1 + \
    1 + 1 \
    + 1
print(x_escape_seq) # resultado 6

#operadores aritmeticos    +   -   *   /   //   %   **
potencia_cuadrada = 5 ** 2 # resultado 25
division_real = 19/3 # da de resultado 6.33 periodico
division_entera = 19//3 # da de resultado 6
modulo_division = 19 % 3 # da de resultado el resto de hacer 19/3, es decir "1"

# operadores de comparacion > >= < <= == !=
# operadores logicos AND OR NOT XOR
# operadores CON CADENAS * y +   ejemplo: 3*'A' ('AAA') , 'A'+'B' ('AB')

# podemos corroborar la clase (o tipo) de una variable con el comando type(variable)
entero = 10
print( type(entero) )

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
# llave : valor
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
caracter_convertido_a_entero = ord(caracter) #(valor resultado: 97)
cadena_convertido_en_numero_complejo = complex("10+5j")
#caso bool(): el 0 y el None lo convierte en "False". 
# El resto en "True".
booleano_True = bool("Cualquier cosa")
booleano_False = bool(0); 
booleano_False2 = bool(None); 
# podemos corroborar el tipo de una variable con el comando type(variable)
print(type(entero))

# FUNCIONES STRINGS
# To check if a certain phrase or character is present in a string, we can
#  use the keyword in.
txt_ = "hola mundo"
if ("mundo" in txt_):
    print("'mundo' existe en txt_")
if ("auto" not in txt_):
    print("'auto' no existe en txt_")

# SLICING
# You can return a range of characters by using the slice syntax
# Get the characters from position 2 to position 5 (not included):
print(txt_[2:5]) # 'la '
# imprimir ultimo caracter
print(txt_[-1]) # 'o'

# metodos
# https://www.w3schools.com/python/python_strings_methods.asp

# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to
#  insert.
# An example of an illegal character is a double quote inside a string that
#  is surrounded by double quotes:.
txt_ = "We are the so-called \"Vikings\" from the north."
# https://www.w3schools.com/python/python_strings_escape.asp


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
suma_ = 0
n = int(input('Ingrese tope maximo: '))
while (cont <= n):
    suma_ = suma_ + cont
    cont = cont + 1
print('La suma total es: ', suma_)

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

# sin contador aux
lista_auxiliar = ["a", "b", 1, 2, 3]
for i,elemento in enumerate(lista_auxiliar):
    print(f"El elemento numero {i} de la lista es {elemento}") #{lista_auxiliar[i]}")
    i+=1
print("Fin FOR")

# FOR con tipos "range()"
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
# Al aparecer un continue en Python, este regresa al comienzo del bucle,
# ignorando todas las sentencias/lineas de codigo que quedan en la
# iteración actual del bucle e inicia la siguiente iteración.

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

# If the number of arguments is unknown, add a * before the parameter name:
# ex: ( https://www.w3schools.com/python/python_functions.asp )
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


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
def funcion5_(parametro2, parametro3, parametro1 = 1):
    '''funcion con VALORES POR DEFECTO'''
    # los parametros tienen valores por defecto en caso de que no se asignen
    return parametro1 + parametro2 + parametro3

print(f"Suma de 1, *7* y *13*: {funcion5_(parametro2 = 7, parametro3 = 13)}")


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


# FUNCIONES COMO ARGUMENTO
# pasando una funcion como parametro de otra funcion.
# En este ejemplo paso la funcion 'condicion' que permite 
# filtrar en otra funcion segun alguna condicion 'x'.
# https://www.youtube.com/watch?v=YgXnSWG2_AY&list=PLF8hyxwQo59jdYDjY4dpseCdsANSakqT3&index=13
def filtro(numeros, condicion):
    '''
        Toma una lista de numeros como primer parametro y una funcion 
        de condicion para el filtro en el segundo parametro.
    '''
    resultado = list()
    for numero in numeros:
        if condicion(numero):
            resultado.append(numero)
    return resultado

numeros = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def es_par(x):
    return x % 2 == 0

def es_negativo(x):
    return x < 0

print( filtro(numeros,es_par), end='\n\n' )

print( filtro(numeros,es_negativo) )

# podemos usar la funcion por defecto FILTER de forma similar, solo 
# que FILTER devuelve un ITERADOR (creo que se ve mas adelante), por lo 
# que hay que transformarlo en lista para ver su resultado.
# solo que tiene un orden de parametros distintos, pasar primero la funcion!

filtro_1 =  filter(numeros, es_par)
print( list(filtro_1) , end='\n\n')

filtro_2 = filter(numeros, es_negativo)
print(list(filtro_2))


# Funciones con una cantidad indeterminada de argumentos
# es una alternativa a pasar una lista o otro iterable como
# argumento de una funcion.


# Argumentos indeterminados 
# En alguna ocasión no podremos determinar previamente cuantos elementos
# se necesita enviar a una función. En estos casos se puede utilizar los
# ​argumentos indeterminado​s por posición y por nombre

# 1) por posicion (lista dinamica)
def indet_posicion(*args):
    '''Imprime valores pasados por parametros'''
    for arg in args:
        print(arg)
# *args es una TUPLA, en donde el operador * es de 'unpacking'
# esa tupla va ACUMULANDO los valores que le pasamos. Siempre que 
# estos valores no los puedan tomar otros parametros de la funcion
#   https://www.youtube.com/watch?v=7a3d0Du3OHc&list=PLF8hyxwQo59jdYDjY4dpseCdsANSakqT3&index=13&ab_channel=CommitThatLine%21

lista_x1 = [1, 2,["a","b"], 4]
indet_posicion(*lista_x1)

# 2) por nombre
def indet_nombre(**kwargs):
    '''Imprime valores pasados por parametros'''
    for key, value in kwargs.items():
        print(f"key: {key}, value: {value}")
        
diccionario_x1 = {"a":"A", "b": "B"}
indet_nombre(**diccionario_x1)




# orden en el que se escriben los parametros para una funcion por defecto:
# https://youtu.be/49eS__KMlpo?si=ZK54Njc7qYjeasQP&t=335
def funcion_argumentos(
    argumento1, argumento2, # argumentos posicionales (obligatorios al invocar la funcion)
    *args_indeterminados_por_posicion, 
    arg_defecto_1=True, arg_defecto_2='Manzana',
    **kwargs_indeterminados_por_nombre
):
    print(argumento1, ' | ', argumento2)
    for arg in args_indeterminados_por_posicion:
        print(arg)
    print(arg_defecto_1, arg_defecto_2)
    for key,value in kwargs_indeterminados_por_nombre.items():
        print('key: ',key,' | value: ',value)


funcion_argumentos('arg1', 'arg2', 1, 2, 3, 4, 5, arg_defecto_2='No es una manzana',
                   uno=1, dos=2, tres=3)

###############################################################################
###############################################################################
###############################################################################
# ejemplo completo hecho a mano para practicar
def func_describe_persona(nombre, 
              *args_nombre_mascotas, 
              nacionalidad='Arg',
              caracteristica=954, 
              **kwargs_datos_extra
):
    print('*'*90)
    print(f'nombre: {nombre}')
    if args_nombre_mascotas:
        print('nombre mascotas:')
        i=1
        for mascota in args_nombre_mascotas:
            print(f'mascota {i}:',mascota)
            i+=1
    else:
        print('no tiene mascotas')
    print('Nacionalidad:',nacionalidad,'. Caract:', caracteristica)
    if kwargs_datos_extra:
        print('datos adicionales:')
        for key in kwargs_datos_extra:
            print(key, kwargs_datos_extra[key])
    else:
        print('no se indicaron datos adicionales')
    print('*'*90)

func_describe_persona('John','Stuart','Alonso','Asu',nacionalidad='American'
                      ,caracteristica=999, age=29, hobbies='caminar')

func_describe_persona('Juan', #'Stuart','Alonso','Asu',nacionalidad='American'
                              #,caracteristica=999, age=29, hobbies='caminar'
                      )

func_describe_persona('Alan', 'Fidel', #nac
                      caracteristica=7888,
                      gustos=['vino','escalar','caminar']
                      )
###############################################################################
###############################################################################
###############################################################################



###############################################################################
###############################################################################
###############################################################################
# otro ejemplo completo generado con Gemini
def resumen_evento(nombre_evento, *invitados, horario="20:00", **detalles_extra):
    """
    Muestra el resumen de un evento.
    
    1. nombre_evento: Posicional (Obligatorio).
    2. *invitados: Recoge todos los nombres extra que pasemos (Tupla).
    3. horario: Valor por defecto. IMPORTANTE: Al estar después de *args,
       se convierte en un argumento 'keyword-only' (solo modificable por nombre).
    4. **detalles_extra: Recoge cualquier par clave=valor sobrante (Diccionario).
    """
    
    print(f"--- REPORTE DEL EVENTO: {nombre_evento.upper()} ---")
    
    # 1. Mostrar invitados (provenientes de *args)
    if invitados:
        print(f"Asistentes ({len(invitados)} personas):")
        for persona in invitados:
            print(f" - {persona}")
    else:
        print(" -> No hay lista de invitados específica.")

    # 2. Mostrar horario (proveniente del valor por defecto o modificado)
    print(f"Horario confirmado: {horario}")

    # 3. Mostrar detalles extra (provenientes de **kwargs)
    if detalles_extra:
        print("Información adicional:")
        for clave, valor in detalles_extra.items():
            print(f" - {clave}: {valor}")
    
    print("-" * 40 + "\n")


# CASO 1: Uso básico (solo lo obligatorio + args)
# 'Cena' va a nombre_evento
# 'Juan', 'Ana', 'Luis' son capturados por *invitados
# horario usa el default "20:00"
# detalles_extra queda vacío
resumen_evento("Cena de equipo", "Juan", "Ana", "Luis")


# CASO 2: Modificando el valor por defecto y añadiendo extras
# Nota como para cambiar el horario, ESTOY OBLIGADO a poner 'horario=' explícitamente
# porque *invitados se "come" todo lo que sea posicional.
resumen_evento(
    "Hackathon",           # nombre_evento
    "Pedro", "Maria",      # *invitados
    horario="09:00 AM",    # Argumento por defecto modificado (Keyword-only)
    ubicacion="Oficina",   # **detalles_extra
    requiere_laptop=True,  # **detalles_extra
    comida="Pizza"         # **detalles_extra
)
###############################################################################
###############################################################################
###############################################################################


# type hints (sigue funciones)
# https://docs.python.org/3/library/typing.html
# https://towardsdatascience.com/12-beginner-concepts-about-type-hints-to-improve-your-python-code-90f1ba0ac49
# se puede indicar mediante una pista el tipo de dato esperado para una funcion
# esto es interpretable por el VS Code
def funcion5(quiero_lista : list, quiero_lista_de_strings : list[str]):
    pass # Para evitar errores cuando la funcion no hace nada
lista = [1, 2, 3]
lista_strings = ["1", "2", "3"]
funcion5(lista, lista_strings)

# tambien se puede indicar que tipo de valor devuelve la funcion
#   en este caso se indica que la funcion devuelve un entero
def suma(a:int, b:int) -> int:
    return a + b

# si quisieramos indicar mas de un tipo posible de entrada/devolucion
#   usariamos el simbolo "|" 
def suma2(a:int|float, b:int|float) -> int|float:
    return a + b
    # probar pasar mouse por encima de "a", "b" y "suma2"

# usamos ''' para hacer comentarios de ayuda
def suma3(a:int, b:int) -> int:
    '''
    COMENTARIO: suma 2 valores a y b
    '''
    return a+b


# tambien podemos usar un ALIAS para los tipos. Ej: listas anidadas de enteros
lista_enteros = list[int]
lista_anidada_2_niveles = list[lista_enteros]
def recibe_lista_anidada(lista_ani : lista_anidada_2_niveles):
    pass # Para evitar errores cuando la funcion no hace nada

lista_anid = [[1, 2, 3], [4, 5]]
lista_anid2 = [[1.0, 2.0, 3.0], [4.0, 5.0]]
recibe_lista_anidada(lista_anid)
# probar pasar mouse por encima de "lista_anidada_2_niveles"
# se puede configurar la extension PYLANCE para detectar diferencias de tipos
# https://www.emmanuelgautier.com/blog/enable-vscode-python-type-checking

# por ultimo, tambien se puede indicar el tipo de una variable usando 
# comentarios ( #type: ).  Ej:
def funcion_test():
    diccionario_nuevo = dict() #type: dict[int, str]
    # esto indica que diccionario_nuevo sera un diccionario con claves de tipo "int"
    # y valores de tipo "str"
    



# importar funciones/procedimientos 
# [Este codigo se escribe en el .py principal]
# from ARCHIVO import nombre_funcion
from archivo_funciones import nombre_funcion1, nombre_funcion2

# [Este codigo se escribe en el .py de funciones]
if __name__ == '__main__':
    print("HOLA") # estas lineas codigo solo se van a ejecutar si se 
    # ejecuta la funcion desde la terminal

import archivo_funciones #trae todo el programa como un objeto!
# se usan las funciones escribiendo: 
archivo_funciones.nombre_funcion1

# para importar TODAS las funciones, se usa
from archivo_funciones import *

# ejemplo en    [practicas_varias\importarPracticas\principal.py]
#               [practicas_varias\importarPracticas\funciones_1.py]


########################################################################
########################################################################

# LAMBDA FUNCTIONS
# asked to IA https://www.phind.com/
'''
In Python, a lambda function is a small, anonymous function that can
be defined in a single line of code. It is also known as an inline 
function or a lambda expression. Lambda functions are typically used 
in situations where a named function would be overkill, or where a 
function is needed for a short period of time and doesn't need to be
saved for later use.
'''
# syntax:   lambda arguments: expression
sum = lambda x, y: x + y
print(sum(2, 3))  # Output: 5



# ejemplo de practica mio
def su_suma_es_par(numero1,numero2):
    if ( (numero1+numero2) % 2 == 1):
        return False
    else:
        return True

print('(2 + 1) es par?', su_suma_es_par(2,1))
print('(3 + 3) es par?', su_suma_es_par(3,3))
print('(4 + 3) es par?', su_suma_es_par(4,3))
print('(5 + 1) es par?', su_suma_es_par(5,1))

# ejemplo lambda
lmbd_suma_par = lambda n1,n2: (n1+n2) % 2 == 1
print('lmbd (2 + 1) es par?', lmbd_suma_par(2,1))
print('lmbd (3 + 3) es par?', lmbd_suma_par(3,3))
print('lmbd (4 + 3) es par?', lmbd_suma_par(4,3))
print('lmbd (5 + 1) es par?', lmbd_suma_par(5,1))
# esto NO ES UNA BUENA PRACTICA, ya que para hacer funciones asi usariamos 'def'


# ejemplo y explicaciones, hecho con IA Gemini:
# Las lambdas brillan cuando necesitas pasar una función como argumento a otra función (funciones de orden superior)

# Para entender cómo map o filter usan lambdas, vamos a crear nosotros mismos una función que acepte una lambda.
# Imagina una "Calculadora Universal". Esta calculadora no sabe sumar ni restar, solo sabe recibir dos números y aplicarles una operación que tú le des.

'Paso 1: Definir la función receptora (Orden Superior)'
def calculadora_universal(a, b, operacion):
    """
    a: primer número
    b: segundo número
    operacion: ¡Una función que le pasaremos desde fuera!
    """
    print(f"Recibí los números {a} y {b}")
    print("Ahora voy a ejecutar la operación que me diste...")
    
    # AQUÍ ES DONDE OCURRE LA MAGIA
    resultado = operacion(a, b) 
    # Python toma el argumento 'operacion' y lo usa como una función.
    
    return resultado

'Paso 2: Usarla con una Lambda'
#Ahora llamamos a nuestra calculadora pasándole los números y, en el tercer argumento, inyectamos la lógica usando una lambda.

# Caso A: Usarla para SUMAR
res_suma = calculadora_universal(5, 3, lambda x, y: x + y)
print(f"Resultado Suma: {res_suma}") 
print("---")
# Caso B: Usarla para MULTIPLICAR
res_multi = calculadora_universal(5, 3, lambda x, y: x * y)
print(f"Resultado Multiplicación: {res_multi}")

''' ¿Por qué es esto tan potente?
Si no pudieras pasar funciones como argumentos, tendrías que escribir una función diferente para cada caso:'''
# sumar_numeros(a, b)
# restar_numeros(a, b)
# multiplicar_numeros(a, b)
''' Al usar funciones de orden superior y lambdas, escribes la lógica del flujo una sola vez (calculadora_universal o map) y cambias el comportamiento "al vuelo" inyectando pequeñas lambdas. '''

## EJEMPLOS de uso de lambdas comunes

# 1) filter espera una función que devuelva True o False para decidir qué elementos quedarse de una lista.
# Objetivo: Obtener solo los números pares de una lista.

numeros = [1, 2, 3, 4, 5, 6]
# Sin lambda tendrías que definir una función aparte
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares) # [2, 4, 6]

# 2) map aplica una función a todos los elementos de una lista.
# Objetivo: Duplicar el valor de cada número.
numeros = [1, 2, 3, 4]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles) # [2, 4, 6, 8]


# 3) Sorted. A veces quieres ordenar una lista de formas complejas, por ejemplo, ordenar una lista de tuplas basándote en el segundo elemento.
# Objetivo: Ordenar productos por precio (el segundo valor).
productos = [
    ('Leche', 1.50),
    ('Pan', 1.00),
    ('Huevos', 2.50)
]
# Ordenamos basándonos en el índice 1 (el precio)
productos_ordenados = sorted(productos, key=lambda x: x[1])
print(productos_ordenados)
# [('Pan', 1.0), ('Leche', 1.5), ('Huevos', 2.5)]

# 4) min() y max() con el parámetro key. por defecto, max() busca el número más alto, pero... ¿y si quieres buscar el objeto con la propiedad más alta?
# Objetivo: Encontrar la palabra más larga.
palabras = ["python", "sol", "elefante", "pez"]

# Si usamos max normal, devolvería 'sol' (por orden alfabético)
# Pero queremos por longitud:
palabra_larga = max(palabras, key=lambda p: len(p))

print(palabra_larga) 
# Resultado: 'elefante'



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








# https://www.w3schools.com/python/python_lists.asp 
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate
#   members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate
#   members. When we say that tuples are ordered, it means that the items
#   have a defined order, and that order will not change.
# Set is a collection which is unordered, unchangeable*, and unindexed. No
#   duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate
#   members.

# *Set items are unchangeable, but you can remove items and add new items.
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier,
#   dictionaries are unordered.

# set - es un CONJUNTO (posee propiedades de union, diferencia, etc)
# https://es.stackoverflow.com/questions/116372/qu%C3%A9-funci%C3%B3n-tiene-el-operador-en-python

set_ = {1, 2, 3, 4} 
'Nota: puse SET COMPREHESION mas adelante'



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

lista_nueva.insert(3, 2) # inserta '2' en la posicion 3

lista_nueva[1] = 99 # modifica elemento en la posicion 1

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
# lo mismo pero viendo de atras hacia adelante, der a izq (<--)
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

# ej lista anidada gemini ia:
# Definimos una lista que contiene otras listas (matriz)
grupos_de_numeros = [
    [1, 2, 3],  # Primera sublista
    [4, 5, 6]   # Segunda sublista
]
# El bucle accede a cada sublista una por una
for sublista in grupos_de_numeros:
    # 'sublista' ahora vale [1, 2, 3] en la primera vuelta
    # y [4, 5, 6] en la segunda vuelta.
    suma_total = sum(sublista)      # Sumamos los números: 1+2+3 = 6
    cantidad   = len(sublista)      # Contamos cuántos hay: 3
    promedio   = suma_total / cantidad
    print(f"La sublista es {sublista} y su promedio es: {promedio}")




# copiar lista
copia_lista = lista_nueva[:]
copia_lista_v2 = lista_nueva.copy()

# https://www.w3schools.com/python/python_lists_copy.asp 
# como NO copiar una lista:
# lo siguiente NO CREA UNA LISTA NUEVA, sino que crea UN NUEVO APUNTADOR
# A UNA MISMA LISTA! (hace pasaje por referencia) ej:
lista_x = [1, 2, 3]
lista_y = lista_x # esto NO copia una lista
lista_y.append(99)
print(lista_x) #imprime [1, 2, 3, 99] !
# (mas adelante se explica como copiar listas anidadas!)
# spoiler: importando 'copy' y usando       list2 = copy.deepcopy(list1)

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

# eliminar elemento (por indice con DEL y por elemento con REMOVE)
del lista_nueva[0]
del lista_nueva[1:4] # borra elementos del indice 1 al 3 incluido (4 sin incluir)
lista_nueva.remove(99) # borra el elemento "99". SOLO LA PRIMERA COINCIDENCIA!
lista_nueva_ultimo_elemento = lista_nueva.pop()
lista_nueva_segundo_elemento = lista_nueva.pop(1) # elemento en posicion 1

'ej para pruebas:'
lista_nueva_02 = [1, 2, 3, 4, 5, 6]

print('lista nueva:',lista_nueva_02)
lista_nueva_02_ultimo_elemento = lista_nueva_02.pop()
print('lista_nueva_02_ultimo_elemento',lista_nueva_02_ultimo_elemento)
print('lista nueva:',lista_nueva_02)
lista_nueva_02_segundo_elemento = lista_nueva_02.pop(1)
print('lista_nueva_02_segundo_elemento',lista_nueva_02_segundo_elemento)
print('lista nueva:',lista_nueva_02)



#funciones de listas varias
# sum() len() max() min()
# se pueden usar operadores matematicos en listas!
# resultado = una_lista + otra_lista
# https://www.w3schools.com/python/python_lists_methods.asp

# SORT - se le puede indicar segun que clave (key) ordenar una lista!
# https://www.w3schools.com/python/python_lists_sort.asp
# You can customize your own function by using the keyword argument 
#   key = function
# example: Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
# en este caso, cada elemento se le aplica la funcion en 'key' y luego
# ese resultado es el que se usa para hacer el sort! Es decir:
# 1) ["banana", "Orange", "Kiwi", "cherry"]
# 2) [str.lower("banana"), str.lower("Orange"), str.lower("Kiwi"), str.lower("cherry"])
# 3) ["banana", "orange", "kiwi", "cherry"]
# 4) SORT ["banana", "orange", "kiwi", "cherry"]


x = [0,1,2,3,4,5,6,7,8,9]
# manejo de listas similar a los parametros de range(start, stop, step) stop=index
sliced = x[1:8:2]
print(sliced) # [1, 3, 5, 7]



# descubrimiento: list.copy() NO funciona bien cuando la lista posee sublistas!
# para ello mejor hacer 'import copy' y usar el metodo:
#                                            list2 = copy.deepcopy(list1)
def demostracion():
    print("Generada lista 1 (lista de listas)")
    lista1 = [[1,2,3,4], [5,6], [7], [8,9,10,11], []]
    print(f"t0 Lista 1: {lista1}\n")
    print("Lista 2 creada a partir de copia de lista 1 usando copy()")
    print("Se invierte lista 2 usando 'reverse'")
    lista2 = lista1.copy()
    lista2.reverse()
    print(f"t1 Lista 1: {lista1}")
    print(f"t1 Lista 2: {lista2}\n")

    print("Agregados dos elementos (12 y 13) a sublista en posicion 3 de lista 1")
    lista1[3].append(12)
    lista1[3].append(13)
    print(f"t2 Lista 1: {lista1}")
    print(f"t2 Lista 2: {lista2}\n")

    print("Creada lista 3 a partir de lista 1 usando copy()")
    lista3 = lista1.copy()
    print(f"t3 Lista 1: {lista1}")
    print(f"t3 Lista 2: {lista2}")
    print(f"t3 Lista 3: {lista3}\n")

    print("Invertido orden sublistas de LISTA 3 usando 'reverse'")
    for i in range(len(lista3)):
        lista3[i].reverse() 
    print(f"t4 Lista 1: {lista1}")
    print(f"t4 Lista 2: {lista2}")
    print(f"t4 Lista 3: {lista3}")

    print("\nIntento de copiar lista4 de lista1 sin que queden vinculadas")

    lista4 = list()
    for i in lista1:
        lista4.append(i)
    print(f"t5 lista 4: {lista4}")
    print("\nlista 1,2,3 y 4 luego de hacer .append(14) a la ultima sublista de lista1")

    lista1[-1].append(14)
    print(f"t6 Lista 1: {lista1}")
    print(f"t6 Lista 2: {lista2}")
    print(f"t6 Lista 3: {lista3}")
    print(f"t6 lista 4: {lista4}")

    print("\nSegundo intento de copiar lista 5 de lista 1 sin que queden vinculadas")

    lista5 = list()
    for i in lista1:
        lista5.append(i.copy())
    print(f"t7 lista 5: {lista5}")
    print("lista 1,2,3, 4 y 5 luego de hacer .append(15) a la ultima sublista de lista1\n")

    lista1[-1].append(15)
    print(f"t8 Lista 1: {lista1}")
    print(f"t8 Lista 2: {lista2}")
    print(f"t8 Lista 3: {lista3}")
    print(f"t8 lista 4: {lista4}")
    print(f"t8 lista 5: {lista5}")

    print("\n Prueba deepcopy (metodo importado de 'copy')")
    import copy
    lista6 = copy.deepcopy(lista1)
    print(f"t9 Lista 1: {lista1}")
    print(f"t9 Lista 6: {lista6}")

    print("\nappend(16) a ultima sublista de lista1")
    lista1[-1].append(16)
    print(f"t10 Lista 1: {lista1}")
    print(f"t10 Lista 6: {lista6}")

    print("\nConclusion: al copiar listas anidadas importar 'copy' y usar "
            "copia_lista_anidada = copy.deepcopy(lista_anidada)")




# Comparacion entre listas:
# cuando se comparan 2 listas, la "mayor" sera la que tenga el primer elemento
# mayor que la otra lista.
# ejs: 
[2] > [1, 2, 3]                                             # type: ignore
# True 

[1, 2, 2] > [1, 2, 3]                                       # type: ignore
# False

[1] < [1, 2]                                                # type: ignore
# True

a = [1, 2, 3]
b = [1, 2, 3]
print(a is a) # True
b is a                                                      # type: ignore
# False
b == a                                                      # type: ignore
# True



# LIST COMPREHESION
# permite crear listas a partir de iterables usando la siguiente estructura:
#   [ 'expression' for 'elemento' in 'iterable' if 'condicion' ]

#   una lista con los triples de estos numeros:
lista_numeros = [3, 8, 1, 9]
lista_triples = [x*3 for x in lista_numeros] # "por cada X en lista_numeros, agregame un x*3 en lista_triples"

# ej: todos los números pares desde el 0 al 100
pares = [x for x in range(0,101) if x % 2 == 0]

# ej: todos los cuadrados de los números pares (del 0 al 100)
pares_cuadrado = [x**2 for x in range(0,101) if x % 2 == 0]

# syntax ( https://www.w3schools.com/python/python_lists_comprehension.asp )
# newlist = [expression for item in iterable if condition == True]
# The iterable can be any iterable object, like a list, tuple, set etc.
# The expression can also contain conditions, not like a filter, but as a way
#   to manipulate the outcome

# example: Return "orange" instead of "banana":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
# The expression in the example above says:
# "Return the item if it is not banana, if it is banana return orange".




# LIST COMPREHESION IF/ELSE (sacado con Gemini IA)
# Si quieres cambiar el valor basándote en una condición (en lugar de filtrar), la estructura if/else va al principio, dentro de la expresion.
# [resultado_si_verdadero if condicion else resultado_si_falso for elemento in iterable]

# Ejemplo: Etiquetar pares e impares
numeros = [1, 2, 3]
etiquetas = ["Par" if n % 2 == 0 else "Impar" for n in numeros]
print(etiquetas)
# Salida: ['Impar', 'Par', 'Impar']







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

# imprimir claves
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

# nota: para copiar el valor de estas 'vistas' podemos meterlos en una lista nueva por ej
lista_claves = list(d.keys()) # x1






# DICTIONARY COMPREHENSION (Hecho con Gemini IA)
# {clave : valor    for     elemento in iterable}
# Ejemplo 1: Cuadrados (versión Diccionario)
# Queremos un diccionario donde la clave sea el número y el valor sea su cuadrado.

# {clave : valor ... }
cuadrados_dict = {i: i**2 for i in range(5)}
print(cuadrados_dict)
# Salida: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# ejemplo 2: Creando diccionarios desde dos listas (con zip)
# nota: vemos 'ZIP' mas adelante

nombres = ['Ana', 'Carlos', 'Beatriz']
edades = [25, 30, 22]
# Usamos zip para unir ambos iterables
agenda = {nombre: edad for nombre, edad in zip(nombres, edades)}
print(agenda)
# Salida: {'Ana': 25, 'Carlos': 30, 'Beatriz': 22}


# Ejemplo 3: Filtrado con if (Condicional al final)
precios = {'leche': 120, 'pan': 45, 'manzana': 30, 'carne': 200}
# Filtramos: Solo guardamos si el precio es menor a 50
ofertas = {k: v for k, v in precios.items() if v < 50}
print(ofertas)
# Salida: {'pan': 45, 'manzana': 30}


# ejemplo 4: Modificación de Valores con if/else
palabras = ['Python', 'es', 'genial', 'si']
clasificacion = {p: ("Larga" if len(p) > 3 else "Corta") for p in palabras}
print(clasificacion)
# Salida: {'Python': 'Larga', 'es': 'Corta', 'genial': 'Larga', 'si': 'Corta'}


# ejemplo 5: Transformación de Claves (Keys) A MAYUSCULAS
datos = {'nombre': 'Juan', 'ciudad': 'Madrid'}
datos_mayus = {k.upper(): v for k, v in datos.items()}
print(datos_mayus)
# Salida: {'NOMBRE': 'Juan', 'CIUDAD': 'Madrid'}

''' !!!
IMPORTANTE 
En los diccionarios, las CLAVES deben ser UNICAS. 
Si tu comprensión genera dos claves iguales, la última que se genere SOBRESCRIBIRA a la anterior.
'''


# uso de ZIP
'''
Entender zip es fundamental porque es el "pegamento" que usamos constantemente en Python para unir datos.
Olvida por un momento los archivos comprimidos .zip (como WinRAR o WinZip). En programación Python, la función zip recibe su nombre del cierre (cremallera) de una chaqueta.

La Metáfora del Cierre
Imagina que tienes dos filas de dientes en un cierre:
* Fila izquierda: Una lista de Nombres.
* Fila derecha: Una lista de Apellidos.

Cuando subes el cierre (zip), los dientes se unen uno a uno en pares perfectos. El primer diente de la izquierda con el primero de la derecha, el segundo con el segundo, y así sucesivamente.

Funcionamiento:
zip() toma dos o más "iterables" (listas, tuplas, etc.) y DEVUELVE UN ITERADOR que genera tuplas con los elementos emparejados por su índice (posición).
'''
nombres = ["Ana", "Bob", "Clara"]
edades = [25, 30, 22]
# Aplicamos zip
combinado = zip(nombres, edades)
# Para ver el resultado, lo convertimos a lista
print(list(combinado)) # [('Ana', 25), ('Bob', 30), ('Clara', 22)]

'''
notas importantes: 
1) Si intentas unir dos listas de tamaños diferentes, zip dejará de funcionar en cuanto se acabe la lista más pequeña. Los elementos sobrantes de la lista larga simplemente se ignoran.
2) Puedes unir más de dos listas. No estás limitado a pares. Puedes hacer un "zip" de 3, 4 o más listas a la vez.
'''






# SET COMPREHESION 
# (lo puse en esta parte del apunte por cuestiones de que esta bueno saber LIST y DICT COMPREHESION antes)
# hecho con Gemini IA
'''
Es muy parecida a lo que ya vimos en dict y list comprehesion
pero tiene un "superpoder" especial: Elimina duplicados automáticamente

Sintaxis Básica: Usa llaves { } como los diccionarios. Pero NO usa dos puntos : (clave:valor), se ve como una lista por dentro.

{ expresion  for  elemento  in  iterable }

ELIMINA AUTOMATICAMENTE DUPLICADOS 
En Python, un set (conjunto) es una colección desordenada de elementos únicos. Si intentas meter el mismo valor dos veces, el conjunto simplemente ignora el segundo.
'''
# Ejemplo: Limpiando una lista de números repetidos
# Imagina que tienes una lista de una encuesta y la gente respondió varias veces lo mismo.
respuestas = [10, 20, 10, 30, 20, 40, 10]
# Creamos el set
unicos = {n for n in respuestas}
print(unicos)
# Salida: {40, 10, 20, 30}
''' Nota: el orden de salida no está garantizado (los sets son desordenados)

Ejemplo Práctico: Normalización de Texto
Este es el caso de uso más común. Tienes una lista de palabras escritas de formas distintas (mayúsculas/minúsculas) y quieres saber cuántas palabras únicas hay realmente.
'''
frutas = ["Manzana", "manzana", "PERA", "Pera", "pera", "Uva"]
# Convertimos todo a minúscula dentro del set comprehension
frutas_unicas = {f.lower() for f in frutas}
print(frutas_unicas)
# Salida: {'manzana', 'pera', 'uva'}


'''Filtrado con if: puedes filtrar antes de agregar al conjunto.'''
# Queremos los cuadrados de los números, pero SOLO si el cuadrado es menor a 100
# y queremos evitar repetidos si la lista original los tuviera.
numeros = [2, 5, 2, 12, 5, 8] # Hay repetidos
cuadrados_bajos = {n**2 for n in numeros if n**2 < 100}
print(cuadrados_bajos)
# Salida: {64, 25, 4}
# (4 viene del 2, 25 viene del 5, 64 viene del 8. El 144 del 12 se filtró).



# nota: no existe 'tuple/tupla comprehension'
 





# ////////
if (1, 2): 
    print("test")
# python considera cumplido el IF si lo que esta dentro NO es None
# (eso en caso de que NO HAYA CONDICIONALES)
# ////////




# ERRORES Y EXCEPCIONES
# Ejemplo de try - catch ('except' en python) dentro de bucle While
bandera = False
while(True):  
    try:
        n = float(input("Introduce un número: "))
        m = float(4)
    #   print("{}/{} = {}".format(n,m,n/m))
        print(f"{n}/{m} = {n/m}")
    except:
        print("Ha ocurrido un error, introduce bien el número") 
    else:
        print("Todo ha funcionado correctamente")
        bandera = True
    finally:
        print("Fin de la iteración") # Siempre se ejecuta

    if bandera: 
    # Importante romper la iteración si todo ha salido bien
        break

# Guardar la excepcion en una variable para analizar el tipo de error segun
# su id, o decidir que hacer segun dicha id
try:
    n = input("Introduce un número: ") # no transformamos a número
    x = 5/n                                                 # type: ignore
except Exception as e: # guardamos la excepción como una variable 'e'
    print("Ha ocurrido un error =>", e) # unsupported operand type(s) for /: 
    #                                     'int' and 'str'
    print("Tipo de error:", type(e).__name__) # TypeError 
    #                                           nos indica el tipo de error

# Gracias a los identificadores de errores podemos crear múltiples
#  comprobaciones, siempre que dejemos en último lugar la excepción
#  por defecto Excepción que engloba cualquier tipo de error (si la
#  pusiéramos al principio las demás excepciones nunca se ejecutarán): 
try:
    n = float(input("Introduce un número divisor: "))
    x = 5/n
except TypeError:
    print("No se puede dividir el número entre una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un número")
except ZeroDivisionError:
    print("No se puede dividir por cero, prueba otro número")
except Exception as e:
    print("Ha ocurrido un error no previsto", type(e).__name__ )

# En algunas ocasiones quizá nos interesa llamar un ​error manualmente​,
#  ya que un ​print común no es muy elegante. Para ello existe una palabra
#  reservada llamada '​raise' ​con la cual podemos lanzar un error manual
#  pasándole el identificador.
# Luego simplemente podemos añadir un ​except ​para tratar esta excepción
#  que hemos lanzado:
def funcion01(valor_no_nulo = None):
    try:
        if valor_no_nulo is None:
            raise ValueError("Error! No se permite un valor nulo") 
                    # este mensaje se puede ver con el debugger de VS Code
        print("Esta parte de codigo NO se ejecuta.")
    except ValueError:
        print("Error! No se permite un valor nulo (desde la excepción)")
funcion01()		




# ASSERT
# assert es como un punto de control de sanidad o un "autochequeo" que pones en tu código
# sintaxis:
'assert condicion, "Mensaje de error opcional"'

# ejemplo:  Comprobando logica interna de programa con descuentos.
# Segun mi logica, el descuento nunca debe ser negativo ni mayor al 100% (1.0)

def aplicar_descuento(precio, descuento):
    # Aseguramos que el descuento sea lógico antes de calcular
    assert 0 <= descuento <= 1, f"El descuento {descuento} es imposible (debe estar entre 0 y 1)"
    
    precio_final = precio * (1 - descuento)
    return precio_final

# Caso correcto
print(aplicar_descuento(100, 0.2))  # Salida: 80.0

# Caso que rompe la lógica (lanza AssertionError)
print(aplicar_descuento(100, 1.5))  # El programa se detiene aquí.

# Importante: assert está diseñado para encontrar errores del programador (bugs), no errores del usuario. Se usa para debugging o chequear cuestiones internas.

# si lo que queremos es, en cambio, chequear si el usuario puso un dato mal o manejar errores en produccion, usamos 'if ... raise'



# 
# POO
# Nota: escribir nombre de las clases en CamelCase (inicio con mayusculas!)

class Producto: # si el nombre fuera mas largo se podria usar ProductoPrincipal,
                # por ejemplo

    # metodo constructor, siempre se ejecuta al crear el objeto
    # los metodos son esencialmente funciones dentro de objetos
    # aplican las mismas reglas (valores por defecto, etc)
    def __init__(self, nombre, precio : float, stock = 0):
        'Crea una instancia de producto'
        self.name = nombre
        self.price = precio
        self.stock = stock
        self.marca = "Marca por defecto" 
    
    # metodos
    def mostrar_nombre(self):
        print(f"Nombre del producto: {self.name}")

    def mostrar_stock(self):
        print(f"Stock del producto: {self.stock}")
    
    def modificar_stock(self, nuevo_stock):
        self.stock = nuevo_stock

    def devolver_stock(self):
        return self.stock
    
    def mostrar_todo(self):
        self.mostrar_nombre()
        print(f'Precio: $ {self.price}')
        self.mostrar_stock()
        print(f'Marca: {self.marca}', end='\n\n')

# INSTANCIACION
# Forma similar a hacer
#   lista_1 = list()

producto1 = Producto("Tornillo", 23.5, 5)
producto2 = Producto("Destornillador", 10, ) # ejemplo tomando valor por
#                                              defecto para el stock

producto1.mostrar_todo()
producto2.mostrar_todo()

# ejemplo, como en funciones, definimos el nombre del parametro al que hacemos
#   referencia
producto3 = Producto(precio= 55.1, stock= 1, nombre= "Tuerca")

producto1.mostrar_nombre()
producto1.mostrar_stock()

producto2.mostrar_nombre()
producto2.mostrar_stock()

producto3.mostrar_nombre()
producto3.mostrar_stock()
print(f"Si sumamos 10 productos tendriamos {producto3.devolver_stock() + 10}"
        " productos en total")


producto4 = Producto("Pintura", 150.5, 15)
## ENCAPSULAMIENTO
producto4.stock = 3     # esto esta MAL
print(f"{producto4.stock}") # esto esta MAL 
# no acceder directamente a la informacion de los atributos

# para eso existe el ENCAPSULAMIENTO
# usamos los METODOS de la CLASE para obtener y usar ATRIBUTOS de un OBJETO
producto4.modificar_stock(10)
producto4.mostrar_stock()

# formas de mostrar el nombre de una clase
class Clase_:
    pass
objeto_ = Clase_()
print(Clase_.__name__) # imprime Clase_
print(type(objeto_).__name__) # imprime Clase_
print(objeto_.__class__.__name__) # imprime Clase_

# imprimir atributos y metodos de una clase
print(objeto_.__dict__) # imprime diccionario de atributos
print(objeto_.__dir__()) # imprime lista con todos los metodos

# Ejemplo con Clase definida mas arriba
print('producto1.__dict__: \n',producto1.__dict__) # imprime diccionario de atributos
print('producto1.__dir__(): \n',producto1.__dir__()) # imprime lista con todos los metodos


# forma de saber si un objeto es instancia de una clase especifica 
# usando isinstance
if isinstance(objeto_, Clase_):
    print(f"El objeto 'objeto_' es de clase '{Clase_.__name__}' ")
# forma de conocer subclases de una clase
# usando issubclass(Clase_hija, Clase_padre)


# ABSTRACCION --> ENCAPULAMIENTO:
# METODOS PUBLICOS Y PRIVADOS
class Ejemplo:
    def publico(self):
        print("Metodo publico de la clase ejemplo.\n")
    def __privado(self): # 2 guiones bajos iniciales
        print("Metodo privado de la clase ejemplo.")
    def usa_privado(self):
        print("Asi se usa un metodo privado:")
        self.__privado()

ej = Ejemplo()
ej.publico()
ej.usa_privado()
# trampa de acceso (#(funciona en la ejecucion xq se renombra!))
ej._Ejemplo__privado()  # type: ignore

# ejemplo de metodos GETTERS y SETTERS
class Ejemplo2:
    def __init__(self, att1, att2, att3):
        self.att1 = att1
        self.att2 = att2
        self.att3 = att3    
    
    # Getters
    def getAtt1(self):
        return self.att1
    def getAtt2(self):
        return self.att2
    def getAtt3(self):
        return self.att3
    
    # Setters
    def setAtt1(self, att1):
        self.att1 = att1
    def setAtt2(self, att2):
        self.att2 = att2
    def setAtt3(self, att3):
        self.att3 = att3
        
# Nota: hice un programa que genera estos automaticamente en 
# D:\CURSOS\Informatorio\INFORMATORIO2022\prog_web
#   \01_python\practicas_02_adicional_informatorio\
#   practicas_varias\auto_getters_setters_py\auto_getter_setter.py
# Nota: Podes utilizar el atributo especial de clase name para recuperar el
#   nombre de la clase de un objeto:      type(objeto).__name__


# HERENCIA
# En el diseño de jerarquías de herencia no siempre es del todo fácil decidir
#  cuándo una clase debe extender a otra. La regla práctica para decidir si
#  una clase (S) puede ser definida como heredera de otra (T) es que debe
#  cumplirse que "S es un T". Por ejemplo, Perro es un Animal, pero Vehiculo
#  no es un Motor.

# Para indicar que una clase hereda de otra se coloca el nombre de la clase de
#  la que se hereda entre paréntesis después del nombre de la clase:
class Instrumento:
    def __init__(self, precio):
        self.precio = precio

class Bateria(Instrumento):
    pass

# sobreescribir metodos
# ej: agregar instrucciones extra al init de Guitarra que hereda de Instrumento.
# Escribimos un nuevo método ​__init__ para la clase Guitarra que se ejecutaría
#    en lugar del ​__init__​ de Instrumento
# sintaxis ​SuperClase.metodo(self, args) 
# o sino    super().metodo(args) << NO RECOMENDADO SI HAY HERENCIA MULTIPLE
#                                   (ver mas adelante)

class Guitarra(Instrumento):
    def __init__(self, tipo_cuerda, precio):
        Instrumento.__init__(self, precio)
       # super().__init__(precio) # hace lo mismo
        self.tipo_cuerda = tipo_cuerda

    # tambien se ocupa para sobreescribir metodos como los que vienen por defecto
    # ejemplo
    def __str__(self) -> str:
        return ("Tipo de cuerda: " + self.tipo_cuerda + ", precio: "
                + str(self.precio))
# aqui se imprimirian sus atributos al hacer un print:
gui = Guitarra("metalica", 100)
print(gui)

# Herencia multiple
# es posible heredar de varias clases a la vez
class Terrestre:
    def __init__(self):
        pass
    def desplazar(self):
        print("El animal anda")

class Acuatico:
    def __init__(self):
        pass
    def desplazar(self):
        print("el animal nada")

class Cocodrilo(Terrestre, Acuatico):
    pass
# Para aquellos metodos que se repitan en nombre (incluido el __init__),
# La clase Cocodrilo tomata como prioritaria las que esten definidas mas
# a la izquierda (Ej, en este caso usara las clases de Terrestre)


# en caso de que se requiera el uso de el constructor
# de alguna clase específica puede usarse la sintaxis anteriormente vista,
# SuperClase.metodo(self, args)

class Cocodrilo2(Terrestre, Acuatico):
    def __init__(self):
        Acuatico.__init__(self)

# herencia multinivel
# tener en cuenta que se puede heredar de clases derivadas!.
class Figura:
    def __init__(self, area):
        self.area = area
    def retornar_area(self):
        print(f"El area de la figura es: {self.area}")
class Poligono(Figura):
    def __init__(self, lados, area):
        Figura.__init__(self, area)
        self.lados = lados
    def retornar_lados(self):
        print("Los lados del poligono son:", self.lados)  
class Cuadrilatero(Poligono):
    def __init__(self, lados, area):
        Poligono.__init__(self, lados, area)
        

# orden de herencia
# todas las clases derivan de la clase "object"
# En el escenario de herencia múltiple, cualquier atributo especificado se
#  busca primero en la clase actual. Si no se encuentra, la búsqueda
#  continúa en clases primarias en profundidad, de izquierda a derecha,
#  sin buscar la misma clase dos veces.
# Orden busqueda ej anterior: [​Cuadrilatero​, ​Poligono​, ​Figura​, ​object​]
# (A esto se le llama linealizacion de la clase Cuadrilatero)
# Sigue un conjunto de reglas llamado Method Resolution Order (MRO)

# El MRO de una clase puede verse como el atributo ​__mro__ (devuelve una
#  tupla) o el método ​mro()​  (devuelve una lista). 
print(Cuadrilatero.__mro__)
print(Cuadrilatero.mro())
# (<class '__main__.Cuadrilatero'>, <class '__main__.Poligono'>, 
#                       <class '__main__.Figura'>, <class 'object'>)




# This block of code is for using my own functions
# https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
# https://www.codegrepper.com/code-examples/python/python+call+function+from+another+folder
import sys # sys.path is a list of absolute path strings
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))
print(str(pathlib.Path(__file__).parent.parent.resolve()))
# check number of ".parent" doing a print of the STR in the line above
# it has to return something like "...\prog_web\01_python\practicas_02_adicional_informatorio"
import personal_functions
# print(personal_functions.test())


#################################################################################
# continua en 
# \practicas_03_adicional_post_info\apuntes_varios_p2.py