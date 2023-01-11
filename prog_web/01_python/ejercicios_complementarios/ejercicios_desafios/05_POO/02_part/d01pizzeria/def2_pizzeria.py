def check_non_negative_int(x):
    while(True):
        try:
            x = int(x)
            if x < 0:
                print(f"{x} es un valor negativo. Ingresar un valor entero"
                        " mayor o igual a 0:")    
                x = input("\t")  
                continue
            else:
                return x        
        except:
            print(f"{x} no es un valor numerico entero. Volver a ingresar:")
            x = input("\t")

def convert_to_int(x):
    '''
    Use with an input. It checks out if the input is an integer!
    '''
    while(True):
        try:
            return int(x)
        except:
            print(f"El valor {x} no es un numero entero. Reintentar.")
            x = input("\t")
            continue
        
def check_range(x:int, bottom_n:int, top_n:int):
    ''' 
    continues if x is an integer between "bottom_n" and "top_n"
    ex:     check_range(17, 1, 10) makes you change 17 for another number. 
            check_range(5, 1, 10) returns 5. 
    '''
    while(True):
        try:
            if(bottom_n <= x <= top_n):
                return x
            else:
                print(f"{x} no es un valor entero comprendido entre "
                    f"{bottom_n} y {top_n}. Reintentar operacion.")
                x = convert_to_int(input("\t"))
        except:
            x = convert_to_int(input("\t"))

def month_days(month: int, year: int):
    '''
    Returns the amount of days in a month given its year.
    '''
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        if leap_year(year):
            return 29
        else:
            return 28
    else: 
        print("Mes incorrecto (Mes debe valer entre 1 y 12)")
        pass

def leap_year(year: int) -> bool:
    ''' 
    Returns True if the year is a leap year
    ex: 2004 returns True, 2003 returns False
    '''
    if year%4 == 0:
        return True
    else: 
        return False

def return_S_N():
    print("Validar (S - si / N - no)")
    while(True):
        x = input("\t").strip().upper()
        if x in ("S","N"):
            return x
        else:
            print("Carater invalido. Reintentar\n")