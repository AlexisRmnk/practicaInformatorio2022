def ask_sides():
    while(True):
        try: # Exception control
            s1 = float(input("Ingresar lado 1\n\t"))
            s2 = float(input("Ingresar lado 2\n\t"))    
            s3 = float(input("Ingresar lado 3\n\t"))
            return (s1, s2, s3)
        except:
            print("Algun valor introducido es incorrecto. Reintentar")

