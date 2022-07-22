# These are my own personal functions to use on my code

def test():
    '''Just for testing purposes. This prints "HELLO WORLD"'''
    print("HELLO WORLD")

def check_return_int(x:str):
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

def check_return_float(x:str):
    '''
    Use with an input. It checks out if the input is a float!
    '''
    while(True):
        try:
            return float(x)
        except:
            print(f"El valor {x} no es un numero decimal. Reintentar.")
            x = input("\t")
            continue

def check_range(x:int, bottom_n:int, top_n:int):
    ''' 
    continues if x is an integer between "bottom_n" and "top_n"
    ex:     check_range(17, 1, 10) returns False. 
            check_range(5, 1, 10) returns True. 
    '''
    while(True):
        try:
            if(bottom_n <= x <= top_n):
                return x
            else:
                print(f"{x} no es un valor entero comprendido entre "
                    f"{bottom_n} y {top_n}. Reintentar operacion.")
                x = check_return_int(input("\t"))
        except:
            x = check_return_int(input("\t"))
        

def make_menu(*kargs, exit_option = "Exit"):
    '''
    Recieves a tuple of options to construct a quick qenu. 
    There's a second (optional) argument to the 'exit' option.
    It prints the options and return an integer.
    
    Ex: make_menu("insert","update","delete", exit_option="STOP")
    Prints the menu and returns 1, 2 or 3. Or 0 to exit.
    '''
    menu_str = "MENU:\n"
    i = 1
    for arg in kargs:
        menu_str = menu_str + f"\t{i})\t{arg}\n"
        i+=1
    menu_str = menu_str + f"\n\t0)\t{exit_option}"
    print(menu_str)
    # checks if x is integer, then checks if it is in range
    x = check_return_int(input("\t"))
    x = check_range(x, 0, len(kargs))
    return x

# menu_test = make_menu("insert","update","delete", exit_option="STOP")
# print("Seleccionada opcion ", menu_test)



