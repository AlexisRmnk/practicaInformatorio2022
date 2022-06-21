# hacer agenda
# agenda={nombre_ : numero_de_telefono_, ...}
from def_clase12agenda import *

agenda = dict()
while(True):
    x = menu()
    if x == 0:
        break
    elif x == 1:
        search(agenda)
    elif x == 2:
        agenda = add(agenda)
    elif x == 3:
        agenda = modify(agenda)
    elif x == 4:
        agenda = delete(agenda)
    elif x == 5:
        agenda = view(agenda)
        # shows and returns agenda ordered by key (name)
    else:
        print("Valor invalido! Reintentar.")
        continue



    

