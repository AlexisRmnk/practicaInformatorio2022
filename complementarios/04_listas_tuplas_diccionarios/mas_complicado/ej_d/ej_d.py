# En un almacén se guarda mercadería en contenedores. No es posible
#  colocar más de n contenedores uno encima del otro y, no hay área para
#  más de 5 pilas de contenedores. Elabore un programa que permita
#  gestionar el ingreso y salida de contenedores. Note que para retirar
#  un contenedor es necesario retirar los contenedores que están encima
#  de él y colocarlos en otra pila.

# idea: lista de listas
# almacen = [[cont1,cont6],[cont2,cont7][cont3,cont8][cont4,][cont5,]]

from def_ej_d import *

container_num = 0
bool_limit_reached = False
max_stack_height = def_top_limit()
max_stacks = def_max_stacks() # cant maxima de pilas de contenedores
storage = list()
for i in range(max_stacks):
    storage.append(list())

while(True):
    operation = menu()
    if operation == "1":
        if (bool_limit_reached):
            print("OPERACION DENEGADA - LIMITE MAXIMO ALCANZADO "
            f"({max_stack_height * max_stacks} contenedores)")
        else: 
            tuple_ = stack_push(storage, max_stack_height, max_stacks, 
                                container_num)
            storage, container_num, bool_limit_reached = tuple_
    elif operation == "2":
        storage, bool_limit_reached = stack_pop(storage, bool_limit_reached)
    elif operation == "3":
        view_stacks(storage, bool_limit_reached, max_stack_height, max_stacks)
    elif operation == "0":
        print("FIN PROGRAMA")
        break

