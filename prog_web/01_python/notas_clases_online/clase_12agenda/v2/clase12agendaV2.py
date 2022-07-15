# hacer agenda
# datos a guardar en esta agenda: nombre (no debe repetirse),  
#                                 numero de telefono, direccion

# tener en cuenta: la agenda se compone de 2 diccionarios anidados
# agenda = {
#          nombre_contacto : {"num" : "3624 444444", "dir" : "Calle Ctes 123"},
#          nombre_contacto2 : {"num" : "3626 555555", "dir" : "Calle Rios 456"},
#          }

from def_clase12agendaV2 import *

agenda = dict()
while(True):
    x = menu()
    if x == "0":
        break
    elif x == "1":
        search(agenda)
    elif x == "2":
        agenda = add(agenda)
    elif x == "3":
        agenda = modify(agenda)
    elif x == "4":
        agenda = delete(agenda)
    elif x == "5":
        agenda = view(agenda)
        # shows and returns agenda ordered by key (name)
    else:
        print("Valor invalido! Reintentar.")
        continue