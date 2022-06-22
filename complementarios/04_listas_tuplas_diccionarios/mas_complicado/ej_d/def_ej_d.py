#para nuestro caso max_value =  max_stacks
def list_fewer_elements_index(list_: list , max_value = 9**9): 
    '''
    Returns the index of the less full sublist on a list of lists.
    Ex: [[1, 2], [3, 4, 5], [6], [7, 8]] returns index 2.
    '''
    i = 0
    minim_len = max_value + 1
    for sub_list in list_:
        if len(sub_list) < minim_len:
            minim_len = len(sub_list)
            minim_index = i
        i+=1
    return minim_index

def list_most_elements_index(list_: list , min_value = 0): 
    '''
    Returns the index of the most full sublist on a list of lists.
    Ex: [[1, 2], [3, 4, 5], [6], [7, 8]] returns index 1.
    '''
    i = 0
    max_len = min_value
    for sub_list in list_:
        if len(sub_list) > max_len:
            max_len = len(sub_list)
            max_index = i
        i+=1
    return max_index

def stack_push(storage_: list, max_stack_height_: int, max_stacks_: int,
             container_num_: int):
    container_limit = max_stack_height_ * max_stacks_
    print("INDICAR CANTIDAD DE CONTENEDORES A APILAR")
    push_ = int(input("\t"))
    for i in range(push_):
        min_sublist_index_ = list_fewer_elements_index(storage_, max_stack_height_)
        if len(storage_[min_sublist_index_]) < max_stack_height_:
            container_num_ += 1
            storage_[min_sublist_index_].append("C_" + str(container_num_))
        else:
            print(f"LIMITE MAXIMO DE {container_limit} CONTENEDORES ALCANZADO."
            f" No se agregaron {push_ - i} contenedores")
            return (storage_ , container_num_, True)
    print("CONTENEDORES APILADOS")
    if (container_limit == count_sublist_elements(storage_)):
        print(f"LIMITE MAXIMO DE {container_limit} CONTENEDORES ALCANZADO.")
        return(storage_, container_num_, True)
    else:
        return(storage_, container_num_, False)

def def_top_limit():
    print("Indicar limite de apilamiento de contenedores (de 1 en adelante)")
    while(True):
        max_stack_height = int(input("\t"))
        if max_stack_height < 1:
            print("Error, valor menor a 1 ingresado. Reintentar.")
            continue
        else:
            return max_stack_height

def def_max_stacks():
    print("Indicar cantidad maxima de pilas contenedores (de 1 en adelante)"
            " (5 por defecto)")
    while(True):
        max_stack_height = int(input("\t"))
        if max_stack_height < 1:
            print("Error, valor menor a 1 ingresado. Reintentar.")
            continue
        else:
            return max_stack_height

def menu():
    while(True):
        print("Indique operacion:")
        print(  "1) APILAR CONTENEDORES.\n"
                "2) DESAPILAR CONTENEDORES.\n"
                "3) VER ESTADO PILAS.\n"
                "0) SALIR.\n")
        op = input("\t")
        if op not in ("1","2","3","4","0"):
            print("ERROR - Seleccion erronea. REINTENTAR")
            continue
        else:
            return op

def count_sublist_elements(list_:list) -> int:
    '''
    Counts sum of elements of sublists given the parent list
    Ex: [[1, 2], [3, 4, 5], [6], [7, 8]] returns 8.
    '''
    sum_elements = 0
    for sub_list in list_:
        sum_elements += len(sub_list)
    return sum_elements

def stack_pop(storage_: list, bool_limit_reached: bool):
    print("INGRESE CANTIDAD DE CONTENEDORES A DESAPILAR")
    pop_ = int(input("\t"))
    if pop_==0:
        return storage_, bool_limit_reached

    for i in range(pop_):
        max_sublist_index_ = list_most_elements_index(storage_)

        if len(storage_[max_sublist_index_]) > 0:
            storage_[max_sublist_index_].pop()
        else:
            print("NO HAY MAS CONTENEDORES")
            return (storage_ , False)
    print(f"CONTENEDORES DESCARGADOS - QUEDAN "
            f"{count_sublist_elements(storage_)} CONTENEDORES")
    return(storage_, False)

def view_stacks(storage_: list, bool_limit_reached: bool, 
                max_stack_height_: int, max_stacks_: int):
    i=0
    for sub_list in storage_:
        #sub_list.reverse() <- breaks the code
        i+=1
        print(f"\nPILA N°{i}, {len(sub_list)} CONTENEDORES")
        for i in range(len(sub_list)-1, -1, -1):
            print(f"| {sub_list[i]} |")
        print("/"*30)
    print("/"*30)
    containers = count_sublist_elements(storage_)
    container_limit = max_stack_height_ * max_stacks_
    print(f"TOTAL: {containers} CONTENEDORES. QUEDA ESPACIO PARA"
            f" {container_limit-containers} CONTENEDORES MAS")
    if (bool_limit_reached):
        print(f"LIMITE DE {container_limit} ALCANZADO")
