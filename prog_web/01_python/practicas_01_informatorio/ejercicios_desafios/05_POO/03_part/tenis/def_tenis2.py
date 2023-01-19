
def return_S_N():
    print("Validar (S - si / N - no)")
    while(True):
        x = input("\t").strip().upper()
        if x in ("S","N"):
            return x
        else:
            print("Carater invalido. Reintentar\n")
            
def return_1_2(input_:str):
    input_ = input_.strip()
    while(True):
        try:
            input_int = int(input_)
            if input_int not in (1, 2):
                print("¡El valor debe ser 1 o 2! Reintentar:")
                input_ = input("\t")
                continue
            else:
                return input_int
        except:
            print(f"El valor '{input_}' no es un valor numerico entero."
                  " Reintentar: ")
            input_ = input("\t")