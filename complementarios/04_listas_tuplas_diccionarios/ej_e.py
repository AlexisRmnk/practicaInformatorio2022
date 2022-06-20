# Cargar m elementos en una pila, y luego copiarlos en una nueva lista.
stack__ = list()

i = 0
while(True):
    print(f"Ingresar elemento {i} en la pila: (Envie \"CERRAR\" para salir)")
    element_ = input("\t")
    if element_.upper() == "CERRAR":
        break
    i += 1
    stack__.append(element_)

print(f"PILA: {stack__}")
list_ = list()
for j in range(len(stack__), 0, -1):
    list_.insert(0,stack__[j-1])

print(f"LISTA (copia de PILA): {list_}")

