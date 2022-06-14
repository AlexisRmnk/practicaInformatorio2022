# Escribir un programa que pregunte a diferentes personas cuánto conocen
#  sobre contaminación del 1 al 10, almacene estos valores en una lista
#  y los muestre por pantalla ordenados de menor a mayor. 

list_ = list()
person = 1

while(True):
    print(f"PERSONA {person}:")
    print("Cuanto conoce de contaminacion? (Del 1 al 10)")
    x = input("\t")
    list_.append(int(x))
    print("Desea registrar a otra persona? (ENTER PARA SI), '0' PARA SALIR")
    y = input("\t")
    if y == "0":
        break
    else: 
        person += 1

list_.sort()
print("Valores ordenados: ")
print(list_)
