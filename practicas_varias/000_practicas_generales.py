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
N = int(input('Ingrese tope maximo: '))
while (cont <= N):
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




