def menu():
    '''
    Displays a menu
    '''
    print("/"*30)
    print("Seleccione accion a realizar en la agenda tipeando su numero: ")
    print(  "1) buscar un contacto por nombre o numero de telefono\n"
            "2) agregar un contacto\n"
            "3) modificar un contacto\n"
            "4) para borrar un contacto\n"
            "5) para mostrar la agenda completa\n"
            "0) para salir")
    return input("\t")


def add(agenda: dict):
    name_ = input("Ingrese nombre del contacto a agregar:\n\t").title()
    num_ = input("Ingrese numero del contacto a agregar:\n\t")
    dir_ = input("Ingrese direccion del contacto a agregar:\n\t")
    if name_ not in agenda.keys():
        agenda[name_] = dict()
        agenda[name_]["num"] = num_
        agenda[name_]["dir"] = dir_
        print("Contacto agregado!")
    else:
        print(f"Invalido! el nombre {name_} ya se encuentra registrado en"
                f" la agenda. Con el numero {agenda[name_]['num']}.")
    return agenda

def modify(agenda: dict):
    name_ = input("Ingrese nombre del contacto a modificar:\n\t").title()
    if name_ not in agenda.keys():
        print(f"Invalido! el contacto {name_} no existe.")
    else:
        while(True):
            print("Que se desea modificar del contacto?")
            x = input("Ingresar '0' para el nombre, '1' para el numero de"
                        " telefono, '2' para la direccion\n\t")
            if x == "0" or x == "1" or x == "2":
                break
            else:
                print("Seleccion invalida. Reintentar.")
                continue
        if x == "0":
            print(f"Ingresar nuevo nombre para el contacto {name_}")
            name_new = input("\t").title()
            num_aux = agenda[name_]
            del agenda[name_]
            agenda[name_new] = num_aux
            print(f"Contacto modificado! Ahora {name_} se llama {name_new}")
        if x == "1":
            print("Ingresar nuevo numero de telefono para el contacto"
                    f" {name_}")
            num_new = input("\t")
            agenda[name_]["num"] = num_new
            print("Numero modificado!")
        if x == "2":
            print("Ingresar nueva direccion para el contacto"
                    f" {name_}")
            dir_new = input("\t")
            agenda[name_]["dir"] = dir_new
            print("Direccion modificada!")
    return agenda

def delete(agenda: dict):
    name_ = input("Ingrese nombre del contacto a borrar.\n\t").title()
    if name_ not in agenda.keys(): 
        print(f"El nombre {name_} no se encuentra registrado en la agenda.")
    else:
        print(f"Confirmar: Se elminara el contacto {name_} ("
        "'N' para cancelar, ENTER para confirmar)")
        if input("\t").upper() == 'N':
            print("Cancelada eliminacion.")
            return agenda
        else:
            del agenda[name_]
            print(f"Elminado contacto {name_}.")
    return agenda

def order_dictionary(dictionary_: dict):
    '''
    Sorts a dictionary in ascendant order based on its key
    Ex: {"b":8, "c":0, "a":4} -> {"a":4, "b":8, "c":0}
    '''
    keys_ = list(dictionary_.keys())
    keys_.sort()
    dictionary_aux = dict()
    for key_ in keys_:
        dictionary_aux[key_] = None
    for key, value in dictionary_.items():
        dictionary_aux[key] = value
    return dictionary_aux

def view(agenda: dict):
    agenda = order_dictionary(agenda)
    for key, value in agenda.items():
        print(f"Nombre de contacto: {key} - Numero: {value['num']}"
                f" - Direccion: {value['dir']}")
    if len(agenda.items()) == 0:
        print("La agenda no contiene contactos.")
    return agenda

def search(agenda: dict):
    while(True):
        print("Seleccione '1' para buscar contacto por nombre")
        print("Seleccione '2' para buscar contacto por numero de telefono")
        x = input("\t")
        if x == "1": 
            name_ = input("Ingresar nombre a buscar: ").title()
            if name_ not in agenda.keys():
                print(f"{name_} no se encuentra registrado en la agenda.")
            else:
                print(f"Contacto encontrado. Nombre: {name_}. Numero de "
                        f"telefono: {agenda[name_]['num']}. Direccion: "
                        f"{agenda[name_]['dir']}")
            break
        elif x == "2":
            num_exists = False
            num_ = input("Ingresar numero a buscar: ").casefold()
            list_values_of_names = agenda.values() # [{"num": "123", "dir":"calle 11"}, ...]
            for dict_values in list_values_of_names:
                if dict_values["num"] == num_:
                    num_exists = True
            if not num_exists:
                print(f"el numero {num_} no se encuentra registrado en la "
                            "agenda.")
            else: # num exists!
                i = 0
                res = ""
                for key, value in agenda.items():
                    if value["num"] == num_:
                        i+=1
                        res = (res + f"Nombre: {key}, numero de telefono: "
                                    f"{value['num']}, direccion:"
                                    f" {value['dir']}\n")
                print(f"Encontrada/s {i} coincidencias:\n{res}")
            break
        else:
            print("Valor incorrecto. Reintentar")
            continue
     