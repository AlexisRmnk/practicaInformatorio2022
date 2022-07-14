def return_1or2():
    while(True):
        print("El producto es perecedero? ('1' --- SI, '2' --- NO)")
        x = input("\t").strip()
        if x not in ("1","2"):
            print("Valor incorrecto, reintentar.")
            continue
        return x
            
    
def return_int(string_:str):
    while(True):
        try:
            int_ = int(string_)
            return int_
        except:
            print("Valor invalido, debe ser numerico entero. Reintentar: ")
            string_ = input("\t")
            continue