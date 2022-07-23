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
#print(personal_functions.test())

from class_desafCAFE import CoffeMaker

def menu():
    cm = CoffeMaker(5)
    while(True):
        op = personal_functions.make_menu("Llenar", "Servir",
                                          "Añadir mas cafe", "Vaciar",
                                          exit_option = "Salir")
        if op == 0:
            print("Finalizando ejecucion")
            break
        elif op == 1:
            cm.fill()
        elif op == 2:
            cm.serve()
        elif op == 3:
            cm.addCoffee()
        else: # op == 4:
            cm.empty()