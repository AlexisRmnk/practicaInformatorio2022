# autogetter y setter for python
# author: Alexis Romaniuk
from defs_auto_getter_setter import *
         
# MAIN
list_of_atts = list_atts()
print("GETTERS Y SETTERS AGRUPADOS:\n")
auto_get_set(list_of_atts)
print("\n\nGETTERS Y SETTERS ALTERNADOS:\n")
auto_get_set2(list_of_atts)

print("\nDesea obtener getters/setters como privado? "
      "'ENTER' para continuar. '0' para salir.")
x = input("\t").strip()

if x != "0":
    print("GETTERS Y SETTERS PRIVADOS AGRUPADOS:\n")
    auto_get_setV2(list_of_atts)
    print("\n\nGETTERS Y SETTERS PRIVADOS ALTERNADOS:\n")
    auto_get_set2V2(list_of_atts)

print("\nFINALIZANDO EJECUCION")
