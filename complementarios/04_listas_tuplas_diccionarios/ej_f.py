# Cargar k elementos en una cola, y luego copiarlos en una nueva lista.

queue_ = list()
i = 0
while(True):
    print(f"Ingresar elemento {i} en la cola: (Envie \"CERRAR\" para salir)")
    element_ = input("\t")
    if element_.upper() == "CERRAR":
        break
    i += 1
    queue_.append(element_)

print(f"COLA: {queue_}")
list_ = list()
for j in range(len(queue_)):
    list_.append(queue_[j])

print(f"LISTA: {list_}")