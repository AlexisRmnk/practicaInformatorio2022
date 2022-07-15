# https://sites.google.com/view/nivel1-desafios/condicionales
# desafio 4

print("Seleccionar el tipo de receta que se desee:")
print("Receta 1: Verduras, berenjena, lentejas o apio a eleccion.")
print("Receta 2: Verduras, berenjena, morrón o cebolla a eleccion.")

receta = int(input("Receta elegida (indicar '1' o '2'): "))
ingrediente = ["","",""] #inicializamos la lista con 3 cadenas vacias

if(receta == 1):
    print("Seleccionar 3 ingredientes: entre los siguientes:")
    print("Verduras (1)\nBerenjena(2)\nLentejas(3)\napio(4)")
    for i in range(0,3):
        ingrediente_num = int(input(f"Seleccionar ingrediente {i+1} de 3: "))
        if ingrediente_num == 1:
            ingrediente[i] = "Verduras"
        elif ingrediente_num == 2:
            ingrediente[i] = "Berenjena"
        elif ingrediente_num == 3:
            ingrediente[i] = "Lentejas"
        elif ingrediente_num == 4:
            ingrediente[i] = "Apio"
else:
    print("Seleccionar 3 ingredientes: entre los siguientes:")
    print("Verduras (1)\nBerenjena(2)\nMorron(3)\nCebolla(4)")
    for i in range(0,3):
        ingrediente_num = int(input(f"Seleccionar ingrediente {i+1} de 3: "))
        if ingrediente_num == 1:
            ingrediente[i] = "Verduras"
        elif ingrediente_num == 2:
            ingrediente[i] = "Berenjena"
        elif ingrediente_num == 3:
            ingrediente[i] = "Morron"
        elif ingrediente_num == 4:
            ingrediente[i] = "Cebolla"


print(f"Receta elegida: {receta}.\nIngredientes: {ingrediente[0]},"
        f" {ingrediente[1]}, {ingrediente[2]}.")

