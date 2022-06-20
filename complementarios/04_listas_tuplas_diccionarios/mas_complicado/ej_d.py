# En un almacén se guarda mercadería en contenedores. No es posible
#  colocar más de n contenedores uno encima del otro y, no hay área para
#  más de 5 pilas de contenedores. Elabore un programa que permita
#  gestionar el ingreso y salida de contenedores. Note que para retirar
#  un contenedor es necesario retirar los contenedores que están encima
#  de él y colocarlos en otra pila.

# WIP
def stack_push(storage_: list, max_stack_height_: int, max_stacks_: int,
                push_: int):
    for i in range(push_):
        if len(storage_) < max_stacks_:


        


print("Indicar limite de apilamiento de contenedores (de 1 en adelante)")
while(True):
    max_stack_height = int(input("\t"))
    if max_stack_height<1:
        print("Error, valor menor a 1 ingresado. Reintentar.")
        continue
    else:
        break
max_stacks = 5

# idea: lista de listas
# almacen = [[cont1,cont6],[cont2,cont7][cont3,cont8][cont4,][cont5,]]

