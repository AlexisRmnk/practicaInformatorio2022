# Escribir un programa que pregunte el nombre del usuario en la consola 
# y después de que el usuario lo introduzca muestre por pantalla 
# El nombre ingresado y la cantidad de letras que tiene.

nombre = input("Ingrese su nombre de usuario: ")
print("Su nombre es", nombre, " y tiene", len(nombre), "caracteres.")
print(f"Su nombre es {nombre} y tiene {len(nombre)} caracteres.")