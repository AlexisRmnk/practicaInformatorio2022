# GESTIÓN DE DONACIONES
# https://sites.google.com/view/informatorio-poo/level-stone/level-stone#h.pbeev0bxu6be

from class_d06 import *
from defs_d06 import *

    
while(True):
    print("Indicar nombre del producto.")
    name = input("\t")
    print("Indicar cantidad del producto.")
    amount = return_int(input("\t"))
    print("Indicar cantidad de entidades a considerar.")
    ent = return_int(input("\t"))
    x = return_1or2()
    if x == "1":
        print("Indicar dias para que el producto expire:")
        days = return_int(input("\t"))
        p = Perishable(name, amount, days)
        p.calculate(ent)
    elif x == "2":
        print("Indicar tipo del producto no perecedero:")
        type_ = input("\t")
        np = NonPerishable(name, amount, type_)
        np.calculate(ent)
        
    print("Desea volver a calcular? ('ENTER' para continuar, '0' para salir)")
    x = input("\t")
    if x == "0":
        print("Finalizando ejecucion.")
        break

