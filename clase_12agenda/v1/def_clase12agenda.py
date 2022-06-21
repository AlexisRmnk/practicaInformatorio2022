def menu():
    '''
    Displays a menu
    '''
    print("/"*30)
    print("Seleccione accion a realizar en la agenda tipeando su numero: ")
    print(  "1) buscar un contacto por nombre o por numero de telefono\n"
            "2) agregar un contacto\n"
            "3) modificar un contacto\n"
            "4) para borrar un contacto\n"
            "5) para mostrar la agenda completa\n"
            "0) para salir")
    return int(input("\t"))

def add(agenda: dict):
    name_ = input("Ingrese nombre del contacto a agregar:\n\t").title()
    num_ = input("Ingrese numero del contacto a agregar:\n\t")
    if name_ not in agenda.keys():
        agenda[name_] = num_
        print("Contacto agregado!")
    else:
        print(f"Invalido! el nombre {name_} ya se encuentra registrado en"
                f" la agenda. con el numero {agenda[name_]}.")
    return agenda

def modify(agenda: dict):
    name_ = input("Ingrese nombre del contacto a modificar:\n\t").title()
    if name_ not in agenda.keys():
        print(f"Invalido! el contacto {name_} no existe.")
    else:
        while(True):
            print("Se desea modificar el nombre o el numero de telefono?")
            x = input("Ingresar '0' para el nombre, '1' para el numero de"
                        " telefono")
            if x == "0" or x == "1":
                break
            else:
                print("Seleccion invalida. Reintentar.")
                continue
        if x == "0":
            print(f"Ingresar nuevo nombre para el contacto {name_}")
            name_new = input("").title()
            num_aux = agenda[name_]
            del agenda[name_]
            agenda[name_new] = num_aux
            print(f"Contacto modificado! Ahora {name_} se llama {name_new}")
        if x == "1":
            print("Ingresar nuevo numero de telefono para el contacto"
                    f" {name_}")
            num_new = input("")
            agenda[name_] = num_new
            print("Numero modificado!")
    return agenda

def delete(agenda: dict):
    name_ = input("Ingrese nombre del contacto a borrar.").title()
    if name_ not in agenda.keys(): 
        print(f"El nombre {name_} no se encuentra registrado en la agenda.")
    else:
        print(f"Confirmar: Se elminara el contacto {name_} ("
        "'N' para cancelar, ENTER para confirmar'")
        if input("\t") == 'N':
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
        print(f"Nombre de contacto: {key} - Numero: {value}")
    return agenda

def search(agenda: dict):
    while(True):
        print("Seleccione '1' para buscar contacto por nombre")
        print("Seleccione '2' para buscar contacto por numero de telefono")
        x = input()
        if x == "1": 
            name_ = input("Ingresar nombre a buscar: ").title()
            if name_ not in agenda.keys():
                print(f"{name_} no se encuentra registrado en la agenda.")
            else:
                print(f"Contacto encontrado. Nombre: {name_}. Numero de telefono:"
                        f" {agenda[name_]}")
            break
        elif x == "2":
            num_ = input("Ingresar numero a buscar: ").casefold()
            if num_ not in agenda.values():
                print(f"el numero {num_} no se encuentra registrado en la agenda.")
            else:
                i = 0
                res = ""
                for key, value in agenda.items():
                    if value == num_:
                        i+=1
                        res = res + f"Nombre: {key}, numero de telefono: {value}\n"
                print(f"Encontrada/s {i} coincidencias:\n{res}")
            break
        else:
            print("Valor incorrecto. Reintentar")
            continue
            