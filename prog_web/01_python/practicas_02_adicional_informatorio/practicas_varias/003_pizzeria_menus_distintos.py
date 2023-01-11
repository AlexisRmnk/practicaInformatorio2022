#una pizzeria ofrece pizzas vegetarianas y no vegetarianas. Los ingredientes
# son: 
#   Vegetarianos: Pimiento y Rucula
#   No Vegetarianos: Jamon y Panceta
# Escribir un SW que pregunte al user si quiere una pizza veggie o no, y 
# en funcion de su respuesta le muestre un menu con los ingredientes 
# dispoibles para que elija.
# Solo se puede elegir un ingrediente ademas de la mozzarella y el tomate 
# que estan en todas las pizzas. Al final se debe mostrar por pantalla si
# la pizza elegida es vegetariana o no y todos los ingredientes que lleva.


# Primera forma
# while(True):
#     eleccion = input("Ingrese V para ver el menu vegetariano y N para ver "
#                 " el menu no vegetariano")
#     if (eleccion == "V" or eleccion=="N"):
#         break

# Segunda forma (parece ser mas legible)


eleccion = ""

while( not (eleccion == "V" or eleccion == "N")):
    eleccion = input("Ingrese V para ver el menu vegetariano y N para ver "
                " el menu no vegetariano: ")
    eleccion = eleccion.upper()

while(True):
    if(eleccion == "V"):
        ingrediente = input("Elegir un ingrediente extra:"
                        " Pimiento (P) o Rucula (R): ")
        ingrediente = ingrediente.upper()
        if( ingrediente == "P" or ingrediente == "R"):
            break
    else:
        ingrediente = input("Elegir un ingrediente extra:"
                        " Jamon (J) o Panceta (P): ")
        ingrediente = ingrediente.upper()
        if( ingrediente == "J" or ingrediente == "P"):
            break

diccionarioMenu = {
    "V": "Vegetariana",
    "N": "No Vegetariana"
}

diccionarioMenuV = {
    "P": "Pimiento",
    "R": "Rucula"
}
diccionarioMenuN = {
    "J": "Jamon",
    "P": "Panceta"
}

if (eleccion == "V"):
    print(f"La pizza elegida es {diccionarioMenu[eleccion]} y posee"
    " los siguientes ingredientes: ")
    print(f"{diccionarioMenuV[ingrediente]}, Mozzarella, Tomate.")
else:
    print(f"La pizza elegida es {diccionarioMenu[eleccion]} y posee"
    " los siguientes ingredientes: ")
    print(f"{diccionarioMenuN[ingrediente]}, Mozzarella, Tomate.")