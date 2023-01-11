# experimento: editar objeto desde bucle FOR

# clase experimento con un valor 'value'
class Experimento:
    def __init__(self, val) -> None:
        self.value = val
    
    # editamos metodo para mostrar valor al usar print() o 
    # str(ObjetoExperimento)
    def __str__(self) -> str:
        return "Valor: " + str(self.value)
    def getValue(self):
        return self.value
    def setValue(self, value):
        self.value = value
    
    
# lista de objetos de clase Experimento
exp_list = [Experimento(1), Experimento(2), Experimento(3), Experimento(4), 
            Experimento(1), Experimento(2), Experimento(3), Experimento(4)]

# Forma de mostrar valor 'value' de cada experimento
# (tambien se podria hacer con .getValue())
print("t1: ", [str(item) for item in exp_list] ) 
# list comprehension: [expression for item in iterable if condition == True]

print("Se reemplazaran valores con '2' por '0'")

for objeto_experimento in exp_list:
    if objeto_experimento.getValue() == 2:
        objeto_experimento.setValue(0)
        
print("t2: ", [str(item) for item in exp_list] )


# prueba: borrar valor "3"
for objeto_experimento in exp_list:
    if objeto_experimento.getValue() == 3:
        exp_list.remove(objeto_experimento)

print("t3: ", [str(item) for item in exp_list] )