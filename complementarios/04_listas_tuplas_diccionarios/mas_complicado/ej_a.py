# Ingresar una palabra, carácter por carácter, en una lista y determinar
#  si es palíndromo.
# palindromo: Palabra o expresión que es igual si se lee de izquierda a
#             derecha que de derecha a izquierda.
# ej: Yo hago yoga hoy

while(True):
    string_ = input("Ingresar palabra/s para determinar si es palindromo"
                    " (0 para salir):\n\t")
    if string_ == "0":
        break
    # removes whitespaces and then converts to lowercase
    string_ = string_.replace(" ", "").lower() 

    list_str = list(string_)
    list_aux = list_str.copy()
    list_aux.reverse()

    if (list_aux == list_str):
        print("Es palíndromo")
    else:
        print("No es palíndromo")
