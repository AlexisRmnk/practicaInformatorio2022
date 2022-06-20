# En un almacén se guarda mercadería en contenedores. No es posible
#  colocar más de n contenedores uno encima del otro y, no hay área para
#  más de 5 pilas de contenedores. Elabore un programa que permita
#  gestionar el ingreso y salida de contenedores. Note que para retirar
#  un contenedor es necesario retirar los contenedores que están encima
#  de él y colocarlos en otra pila.

# idea: lista de listas
# almacen = [[cont1,cont6],[cont2,cont7][cont3,cont8][cont4,][cont5,]]

# WIP 
#       Apilamiento = hecho
#       Desapilamiento = pendiente
#       menu de seleccion = pendiente


#para nuestro caso max_value =  max_stacks
def list_fewer_elements_index(list_: list , max_value = 999): 
    '''
    returns the index of the less full sublist on a list of lists
    ex: [[1, 2], [3, 4, 5], [6], [7, 8]] returns index 2
    '''
    i = 0
    minim_len = max_value + 1
    for x in list_:
        if len(x) < minim_len:
            minim_len = len(x)
            minim_index = i
        i+=1
    return minim_index

def stack_push(storage_: list, max_stack_height_: int, max_stacks_: int,
                push_: int, container_num_: int):
    
    for i in range(push_):
        minim_index_ = list_fewer_elements_index(storage_, max_stacks_)
        if len(storage_[minim_index_]) < max_stack_height_:
            container_num_ += 1
            storage_[minim_index_].append("C_" + str(container_num_))
        else:
            print("LIMITE MAXIMO CONTENEDORES ALCANZADO. No se agregaron "
            f"{push_ - i} contenedores")
            return (storage_ , False, container_num_)
    return(storage_, True, container_num_)



print("Indicar limite de apilamiento de contenedores (de 1 en adelante)")
while(True):
    max_stack_height = int(input("\t"))
    if max_stack_height<1:
        print("Error, valor menor a 1 ingresado. Reintentar.")
        continue
    else:
        break
container_num = 0
max_stacks = 5 # cant maxima de pilas de contenedores
storage = list()
for i in range(max_stacks):
    storage.append(list())

print("Test - apilamiento")
while(True):
    xxx = input("enter para continuar - 0 para salir\n\t")
    if xxx == "0":
        break
    print("apilar? indicar cantidad:")
    push__ = int(input("\t"))
    print("Contenedores estado inicial: ", storage)
    storage, bool_, container_num = stack_push(storage, max_stack_height, max_stacks, push__, container_num)
    print("Contenedores estado final: ", storage)





## pruebas - borrar luego de terminar de escribir el programa

# max_stacks = 5
# storage = list()
# for i in range(max_stacks):
#     storage.append(list())

# print(storage)

# storage[0].append(1)
# storage[1].append(2)
# storage[2].append(3)
# storage[3].append(4)
# storage[4].append(5)
# storage[0].append(6)
# storage[1].append(7)
# storage[2].append(8)


# print(storage)

# i = 0
# minim_len = (max_stacks+1)
# for x in storage:
#     if len(x) < minim_len:
#         minim_len = len(x)
#         minim_index = i
#     i+=1
# # pila con menos elementos: storage[minim_index]

# storage[minim_index].append("9")

# print(storage)

# i = 0
# minim_len = (max_stacks+1)
# for x in storage:
#     if len(x) < minim_len:
#         minim_len = len(x)
#         minim_index = i
#     i+=1

# storage[minim_index].append("10")

# print(storage)

