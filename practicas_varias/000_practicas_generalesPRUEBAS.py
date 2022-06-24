import copy

def control_msg(msg: str):
    '''
    Controls that each bracket has its complementary bracket (at the 
    correct order)
    ex: {msg} returns True
        {{msg} returns False
        {msg{msg} } returns False
        {msg}{msg} returns True
    '''
    bracket_opened = False
    for x in msg:
        if x == "{" and bracket_opened == False:
            bracket_opened = True
        elif x == "{" and bracket_opened == True:
            print("Uso incorrecto de caracter '{'")
            return False
        if x == "}" and bracket_opened == False:
            print("Uso incorrecto de caracter '}'")
            return False
        elif x == "}" and bracket_opened == True:
            bracket_opened = False
        if x == "&" and bracket_opened == True:
            print("Uso incorrecto de caracter '&'.")
            return False
    if bracket_opened == False:
        return True
    else:
        print("Uso incorrecto de caracter '{'")
        return False


cadena_prueba = "{hola}{hola mundo}&{aaaaa}"
bool_rta = control_msg(cadena_prueba)
print(f"BOOL RTA: {bool_rta}")
