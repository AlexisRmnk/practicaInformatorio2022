import copy

def menu():
    print("MENU")
    while(True):
        print("Indique operacion:")
        print(  "1) SIMULAR ENCRIPTAR CONJUNTO DE MENSAJES.\n"
                "2) SIMULAR RECIBIR Y DESENCRIPTAR CONJUNTO DE MENSAJES.\n"
                "3) VER ESTADO ACTUAL.\n"
                "4) REINICIAR\n"
                "0) SALIR.\n")
        op = input("\t")
        if op not in ("1","2","3","4","0"):
            print("ERROR - Seleccion erronea. REINTENTAR")
            continue
        else:
            return op

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

def encrypt():
    user_counter = msg_counter = 1
    msg_aux1 = msg_final = ""
    while(True):
        print(f"USUARIO {user_counter} INGRESE SU MENSAJE {msg_counter}:"
        " (NO USE LOS CARACTERES '{', '}' NI '&'")
        msg_temp = input("\t")
        if "{" in msg_temp or "}" in msg_temp or "&" in msg_temp:
            print("Mensaje invalido. Reintentar")
            continue
        msg_temp = "{" + msg_temp + "}"
        msg_aux1 = msg_aux1 + msg_temp
        print("Desea agregar otro mensaje? (ENTER para SI, 'N' para NO)")
        if input("\t").upper() == 'N':
            user_counter+=1
            msg_counter = 1
            msg_final = msg_final + msg_aux1 
            print("Desea agregar otros mensajes para otro usuario?"
                    " (ENTER para SI, 'N' para NO)")
            if input("\t").upper() == 'N':
                # tuple_aux = msg_final.rpartition("&")
                # msg_final = tuple_aux[0] # deletes last '&'
                print("MENSAJE/S ENCRIPTADO CORRECTAMENTE")
                print(f"Mensaje/s: \n\t{msg_final}")
                return msg_final, True
            msg_final = msg_final + "&"
            msg_aux1 = ""
        else:
            msg_counter += 1

def decrypt(encrypted_msg: str):
    if not control_msg(encrypted_msg):
        print("EL MENSAJE ESTA CORROMPIDO")
        return False
    list_encrypted_msg = encrypted_msg.split("&")
    print(f"Hay {len(list_encrypted_msg)} usuarios con mensajes encriptados.")
    view_list = copy.deepcopy(list_encrypted_msg)
    i=0
    for user_encrp_msgs in view_list:
        i+=1
        message_aux = user_encrp_msgs.replace("{","")
        message_aux = message_aux.split("}")
        message_aux.pop()
        #messages = user_encrp_msgs.partition("}")
        print(f"Usuario {i}: posee {len(message_aux)} mensajes.")
        print(f"Esos mensajes son: {message_aux}")
    return False