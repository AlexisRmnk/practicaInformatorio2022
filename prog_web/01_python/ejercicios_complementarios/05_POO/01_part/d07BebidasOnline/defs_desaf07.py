# This block of code is for using my own functions
# https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
# https://www.codegrepper.com/code-examples/python/python+call+function+from+another+folder
import sys # sys.path is a list of absolute path strings
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.parent.parent.resolve()))
# check number of ".parent" using
# print(str(pathlib.Path(__file__).parent.parent.parent.parent.parent.resolve()))
# it has to return something like "...\prog_web\01_python"
import personal_functions
# print(personal_functions.test())

from class_desaf07 import *

def menu():
    d = Deposit()
    while(True):
        op = personal_functions.make_menu("Agregar producto",
            "Eliminar producto",
            "Mostrar informacion",
            "Calcular precio de todas las bebidas",
            "Calcular el precio total de una marca de bebida",
            exit_option = "Salir"        )
        if op == 0:
            print("Finalizando ejecucion.")
            break
        elif op == 1:
            d.add_product()
        elif op == 2:
            d.del_product()
        elif op == 3:
            d.show_products()
        elif op == 4:
            d.sum_products_price()
        else: # op = 5
            d.sum_products_price(True)