# https://sites.google.com/view/informatorio-poo/level-stone/level-stone#h.aq5rs2uakg5d

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

class CoffeMaker:
    def __init__(self, max_capacity, current_amount = 0) -> None:
        self.max_capacity = personal_functions.convert_to_float(max_capacity)
        self.current_amount = personal_functions.convert_to_float(current_amount)
        self.__check_capacity()
    
    def __check_capacity(self):
        while(True):
            if self.current_amount <= self.max_capacity:
                return
            else:
                print(f"Error. La capacidad actual ({self.current_amount}"
                    f" L) no debe ser mayor a la capacidad maxima ("
                    f"{self.max_capacity} L).\nVolver a ingresar capacidad"
                    " actual: ")
                self.current_amount = personal_functions.convert_to_float(input("\t"))
   
    def fill(self):
        self.current_amount = self.max_capacity
        print("Se lleno la cafetera. Capacidad actual: "
              f"{self.current_amount} L") 
    
    def addCoffee(self):
        print("Indicar la cantidad de cafe que se desea agregar:")
        self.current_amount = personal_functions.convert_to_float(input("\t"))
    
    def empty(self):
        self.current_amount = float(0)
        print("Cafetera vaciada.")
    
    def serve(self):
        print(f"Indicar la cantidad a servir (cantidad actual: "
              f"{self.current_amount} L)")
        to_serve = personal_functions.check_non_negative(
            personal_functions.convert_to_float(input("\t")))
        if self.current_amount == 0:
            print("Cantidad insuficiente, cafetera vacia.")
        elif to_serve > self.current_amount:
            print("Cantidad insuficiente, se han servido los ultimos "
                  f"{self.current_amount} L. No se han podido servir "
                  f"{to_serve - self.current_amount} L")
            self.setCurrent_amount(float(0))
        elif to_serve == self.current_amount:
            print(f"Se han servido los ultimos {self.current_amount} L")
            self.setCurrent_amount(float(0))
        elif to_serve < self.current_amount:
            remaining = self.current_amount - to_serve
            print(f"Servidos {to_serve} L. Restante: {remaining} L")
            self.setCurrent_amount(remaining)
        
    
    def getMax_capacity(self):
        return self.max_capacity
    def setMax_capacity(self, max_capacity):
        self.max_capacity = max_capacity
    def getCurrent_amount(self):
        return self.current_amount
    def setCurrent_amount(self, current_amount):
        self.current_amount = current_amount