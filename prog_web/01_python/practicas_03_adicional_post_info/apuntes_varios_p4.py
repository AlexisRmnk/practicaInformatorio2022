'''
	Nueva practica de Python. 2026-01-09
'''



# @decoradores
# visto con Gemini IA

# Un decorador es una función que toma otra función como entrada, le añade alguna funcionalidad extra, y devuelve una nueva función.
'''
 !! En Python, las funciones son objetos. Esto significa que puedes pasar funciones como argumentos a otras funciones. !!
Un decorador tiene tres partes principales:

1. La función decoradora (la capa externa).
2. La función envoltorio o wrapper (la capa interna donde ocurre la magia).
3. La función original (la que estás decorando).


¿Para qué sirven? (El problema)
Imagina que tienes 10 funciones distintas y quieres saber cuánto tarda cada una en ejecutarse.

Opción A (Aburrida): Escribir código de cronómetro dentro de las 10 funciones (repetir código 10 veces).

Opción B (Decorador): Creas un decorador "Cronómetro" y simplemente le pones la etiqueta @cronometro encima a las funciones que quieras medir.
'''

# Ejemplo: Vamos a crear un decorador que anuncie cuando una función va a empezar y cuando termina.

def mi_decorador(funcion_original):
    # Esta es la función 'envoltorio' que añade la funcionalidad
    def funcion_envoltorio():
        print("--- Algo está pasando ANTES de llamar a la función ---")
        
        funcion_original()  # Aquí se ejecuta la función original
        
        print("--- Algo está pasando DESPUÉS de llamar a la función ---")
    
    return funcion_envoltorio


# primera opcion, sin decorador
def saludar():
    print("¡Hola mundo!")
# "Envolvemos" manualmente la función
saludar_decorado = mi_decorador(saludar)
saludar_decorado()


# segunda opcion, con decorador
@mi_decorador
def saludar():
    print("¡Hola mundo!")

# Ahora, cada vez que llames a saludar, ya estará decorada
saludar()





# otro ejemplo de decorador mas practico, medir tiempo
# Para que el decorador funcione con cualquier función (tenga o no argumentos), usamos *args y **kwargs.

# EXPLICADO PASO A PASO:
import time

def medir_tiempo(funcion_original): # 1. Recibe la función original (ej: dormir)
    
    # 2. Definimos el mensajero (wrapper). 
    # Acepta los argumentos que iban dirigidos a la función original.
    def wrapper(*args, **kwargs): # NOTE Alexis: esto serian los argumentos de la funcion que estoy decorando, se usa esta forma para que sea bien general la cosa!
        
        # PASO A: Lógica ANTES de la función real
        inicio = time.time()  
        
        # PASO B: Ejecutar la función real
        # Aquí "desempaquetamos" los argumentos y se los damos a la función original.
        # Guardamos lo que la función devuelva en una variable 'resultado'.
        resultado = funcion_original(*args, **kwargs) 
        
        # PASO C: Lógica DESPUÉS de la función real
        fin = time.time()     
        
        print(f"Tiempo total: {fin - inicio} segundos")
        
        # PASO D: Devolver el valor original
        # Si no hacemos esto, la función decorada devolvería 'None' y perderíamos el dato.
        return resultado 
        
    return wrapper # 3. Devolvemos al mensajero listo para trabajar 
'''
Simulemos la ejecución:
Imagina que tienes esta función:
'''
@medir_tiempo
def sumar(a, b):
    time.sleep(1) # Simulamos que tarda 1 segundo
    return a + b

# Tú escribes en tu código:
print(f'Ejecutando "sumar()" con parametros 5 y 10"')
x = sumar(5, 10)
print(f'x vale {x}')

'''
Esto es lo que ocurre internamente, paso a paso:

1. Llamada: Llamas a sumar(5, 10). Como está decorada, en realidad estás llamando a wrapper(5, 10).
2. Recepción: wrapper recibe 5 y 10. Los guarda en args = (5, 10).
3. Paso A (Inicio): wrapper mira el reloj (inicio).
4. Paso B (La llamada real): wrapper dice: "Oye funcion_original (sumar), toma estos argumentos (5, 10) y trabaja".
    a. La función sumar se despierta, suma 5+10, espera 1 segundo y devuelve 15.
    b. wrapper captura ese 15 en la variable resultado.
5. Paso C (Fin): wrapper mira el reloj otra vez (fin) y calcula la resta. Imprime "Tiempo total: 1.001s".
6. Paso D (Retorno): wrapper dice: "Aquí tienes el resultado que me dio la función original". Y devuelve el 15.
7. Final: Tu variable x ahora vale 15.
'''
# ¿Por qué es vital el return resultado dentro del wrapper?
# El decorador debe ser transparente: debe devolver lo mismo que la función original devolvería, para no romper el programa.



# adicional: si quiero puedo hacer que la funcion suma() agarre mas *params asi:
@medir_tiempo
def sumar(*args):
    suma = 0
    for arg in args:
        suma = suma + arg
    time.sleep(1) # Simulamos que tarda 1 segundo
    return suma

# Tú escribes en tu código:
print(f'Ejecutando "sumar()" con parametros 5, 10, 15"')
x = sumar(5, 10, 15)
print(f'x vale {x}')


########################################################################################
########################################################################################

# bloque de codigo que te dice las funciones, variables etc que hay en tu py:

import types

def mostrar_datos_global():
    print(f"{'NOMBRE':<25} | {'TIPO':<20} | {'VALOR/ORIGEN'}")
    print("-" * 70)

    # Usamos list() para crear una copia estática de los ítems
    # Así, si el diccionario global cambia durante el bucle, no afecta nuestra lista.
    copia_de_globals = list(globals().items())

    for nombre, valor in copia_de_globals:
        
        # Omitimos las variables internas (las que empiezan con __)
        if nombre.startswith("__"):
            continue
        
        # Omitimos la variable de la copia misma para no ensuciar la lista
        if nombre == "copia_de_globals":
            continue

        tipo = "Variable"
        
        if isinstance(valor, types.ModuleType):
            tipo = "Librería (Módulo)"
        elif isinstance(valor, types.FunctionType):
            tipo = "Función Usuario"
        elif isinstance(valor, types.BuiltinFunctionType):
            tipo = "Función Built-in"
        elif isinstance(valor, type):
            tipo = "Clase"
            
        # Convertimos el valor a string y lo cortamos si es muy largo para que se vea bien
        valor_str = str(valor)[:50] 
        
        print(f"{nombre:<25} | {tipo:<20} | {valor_str}")

mostrar_datos_global()








