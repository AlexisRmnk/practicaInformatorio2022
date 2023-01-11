# ejercicio integrador: 
# https://sites.google.com/view/informatorio-poo/super-sayayin/tenis

from def_tenis import *
from def_tenis2 import return_1_2

print("Desea simular un partido de tenis de forma:\n\t1) manual o\n\t"
      "2) automatica?")
operation = return_1_2(input("\t\t"))
if operation == 1:
    start_match()
else: 
    simulate_match()



