from class_desaf04v3 import *

def agenda_menu(): # responsabilidad y patrones de diseño (MVC)
    ag = Agenda()
    while(True):
        op = __aux_menu()
        ag.sorts_agenda()
        if op == "0":
            print("Saliendo de agenda")
            return
        elif op == "1":
            ag.add_contacts()
        elif op == "2":
            ag.show_contact_list()
        elif op == "3":
            ag.search_contacts()
        elif op == "4":
            ag.edit_contacts()
        else:
            ag.delete_contacts()
            
def __aux_menu(): 
    while(True):
        print("INDICAR OPERACION:\n\tAñadir contacto\t\t(1)\n\tLista de "
                "contactos\t(2)\n\tBuscar contacto\t\t(3)\n\tEditar contacto"
                "\t\t(4)\n\tEliminar contacto\t(5)\n\n\tCerrar Agenda\t\t(0)")
        x = input("\t").strip()
        if x not in ("0", "1", "2", "3", "4", "5"):
            print("Error. Reintentar ingreso de operacion.")
            continue
        return x