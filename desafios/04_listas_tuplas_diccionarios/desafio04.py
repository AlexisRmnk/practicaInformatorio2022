# Escribir un programa que cargue una tupla con nombres de especie, y 
# para cada nombre de especie imprima el mensaje Hola soy ......, cuidame.

# Modificá el programa anterior y dada una posición inicial p y una
#  cantidad n, imprima el mensaje anterior para los n nombres que se
#  encuentran a partir de la posición i.

def print_species(tuple_species: tuple, position:int = 0):
    k = 0
    for x in tuple_species:
        if k >= position:
            print(f"Hola soy {x}, cuidame.")
        k += 1

species_ls = list()
while(True):
    print("Ingrese nombre de especie animal (0 para terminar)")
    sp_name = input("\t")
    if sp_name == "0":
        print("Terminando operacion de ingreso")
        break
    species_ls.append(sp_name)

species_tp = tuple(species_ls)
print(f"Tupla completa:")
i=0
for x in species_tp:
    print(f"{x} en posicion {i}")
    i+=1
position_ = int(input("Indique posicion inicial de tupla a imprimir:\n\t"))
print_species(species_tp, position_)