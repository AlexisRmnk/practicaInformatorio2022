# Se tiene una lista que contiene mensajes encriptados de varios usuarios.
#  Cada mensaje se encierra entre {}, y para indicar que se terminó el
#  área de mensajes de un usuario se usa un signo &. Indique cuántos
#  usuarios y cuántos mensajes hay en la lista, teniendo en cuenta que
#  todos los mensajes están correctamente formados, es decir comienzan
#  con { y terminan con }. Y que es seguro que al menos exista un usuario
#  en la lista.

from def_ej_f import *

is_encripted = False
while(True):
    menu_selection = menu()

    if menu_selection == "1":
        if is_encripted == False:
            msg_, is_encripted = encrypt()
        else:
            print("Invalido. El mensaje ya fue encriptado")
    elif menu_selection == "2":
        if is_encripted == True:
            is_encripted = decrypt(msg_)
        else:
            print("Invalido. El mensaje ya fue desencriptado")
    elif menu_selection == "3":
        if is_encripted:
            print("Mensaje encriptado - pendiente desencriptar")
        else:
            print("Pendiente encriptar mensaje.")
    elif menu_selection == "4":
        is_encripted = False
        print("Variables reiniciadas.")
    elif menu_selection == "0":
        print("FIN DE PROGRAMA")
        break