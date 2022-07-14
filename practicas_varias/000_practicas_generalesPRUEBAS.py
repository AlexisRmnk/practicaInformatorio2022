def __this_one(op:str): 
        while(True):
            this_one = input(f"Este es el contacto que desea {op}? "
                             f"(S/N)\n\t").upper().strip()
            if this_one not in ("S","N"):
                print("Valor erroneo, reintentar.")
                continue
            else:
                return this_one == 'S'

print(__this_one("TEST"))