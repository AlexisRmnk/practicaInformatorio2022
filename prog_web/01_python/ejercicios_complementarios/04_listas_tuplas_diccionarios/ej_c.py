# Escriba un algoritmo que permita cargar una lista. Y que luego, una
#  vez cargada, controle y sustituya cualquier elemento negativo por 0.

def check_int(string_: str) -> bool:
    try:
        int(string_)
        return True
    except: 
        return False

def check_float(string_: str) -> bool:
    try:
        float(string_)
        return True
    except: 
        return False

i = 1
list_ = list()
while(True):
    print(f"Ingrese elemento n°{i} (tipear \"finalizar\" para salir):")
    element_ = input("\t")
    if element_.lower() == "finalizar":
        i -= 1
        break
    list_.append(element_)
    i += 1

print("Lista inicial: ", list_)
i = 0
for element_ in list_:
    if check_int(element_):
        if int(element_) < 0:
            list_[i] = 0
        else:
            list_[i] = int(element_)
    elif check_float(element_):
        if float(element_) < 0:
            list_[i] = 0
        else:
            list_[i] = float(element_)
    i += 1

print("Lista final: ", list_)