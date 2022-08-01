# Ejercicio 8: Capitalízalo
# Muchas personas no usan letras mayúsculas correctamente, especialmente
#  cuando escriben en dispositivos pequeños como teléfonos inteligentes.
#  En este ejercicio, escribirá una función que capitaliza los caracteres
#  apropiados en una cadena. Una "i" minúscula debe reemplazarse por una
#  "I" mayúscula si está precedida y seguida de un espacio. El primer
#  carácter de la cadena también debe estar en mayúscula, así como el
#  primer carácter no espacial después de un ".", "!" o "?" Por ejemplo,
#  si la función se proporciona con la cadena "¿a qué hora tengo que
#  estar allí? ¿cuál es la dirección?" entonces debería devolver la
#  cadena "¿A qué hora tengo que estar allí? ¿Cuál es la dirección?".
#  Incluya un programa principal que lea una cadena del usuario,
#  la capitalice utilizando su función y muestre el resultado.

# notas importantes:
# capitalizeStringVtest(string_) es una funcion de prueba, ignorarla
# capitalizeStringV1(string_) es una funcion que puede ser entendida sin
#   conceptos de listas ni indices pero que no cumple con la condicion
#   de que una "i" minúscula debe reemplazarse por una "I" mayúscula si 
#   está precedida y seguida de un espacio. 
# capitalizeStringV2(string_) funciona bien para todos los casos pero
#   ocupa ALGUNOS conocimientos sobre listas y arreglos. Podria ser
#   optimizado mas adelante.

# FUNCTIONS
def capitalizeStringVtest(string_): #Test - unused
    for char_ in string_:
        print(char_, end=" >>> \n")
        previous_char_index = int(string_.index(char_) - 1)
        if previous_char_index != -1:
            previous_char = string_[previous_char_index]
        else: 
            previous_char = ""

        next_char_index = int(string_.index(char_) + 1)
        if not(next_char_index > len(string_)-1):
            next_char = string_[next_char_index]
        else:
            next_char = ""       
        print(previous_char)
        print(next_char)
        print()

def capitalizeStringV1(string_): # Read detail below
    '''
    Doesn't use lists and works except for the "I" case
    '''
    previous_char = previous_to_previous_char = new_string = ""
    for char_ in string_:
        if (previous_char == "¿" or previous_char == "." 
            or previous_char == "¡" or previous_char == ""
            or previous_char == "?" or previous_char == "!" 
            or (previous_to_previous_char == "." and previous_char == " ")
            or (previous_to_previous_char == "?" and previous_char == " ")
            or (previous_to_previous_char == "!" and previous_char == " ")):
            char_ = char_.upper()
        new_string = new_string + str(char_)
        previous_to_previous_char = previous_char
        previous_char = char_
    return new_string

def capitalizeStringV2(string_): # Uses lists and works on every case
    new_string = ""
    for index_, char_ in enumerate(string_):
        previous_char_index = index_ - 1
        if previous_char_index != -1:
            previous_char = string_[previous_char_index]
        else: 
            previous_char = ""

        previous_to_previous_char_index = index_ - 2
        if (previous_to_previous_char_index != -2 and
            previous_to_previous_char_index != -1):
            previous_to_previous_char = (
                string_[previous_to_previous_char_index])
        else: 
            previous_to_previous_char = ""

        next_char_index = index_ + 1
        if not(next_char_index > len(string_)-1):
            next_char = string_[next_char_index]
        else:
            next_char = ""
        
        if (previous_char == "¿" or previous_char == "." 
            or previous_char == "¡" or previous_char == ""
            or previous_char == "?" or previous_char == "!" 
            or (previous_to_previous_char == "." and previous_char == " ")
            or (previous_to_previous_char == "?" and previous_char == " ")
            or (previous_to_previous_char == "!" and previous_char == " ")
            or (char_ == "i" and previous_char == " " and next_char == " ")):
            char_ = char_.upper()
        new_string = new_string + str(char_) 
    return new_string


# MAIN PROGRAM
print("Ingrese un cadena de texto para capitalizar segun las siguientes reglas:")
print('Una "i" minúscula debe reemplazarse por una'
        '"I" mayúscula si está precedida y seguida de un espacio. El primer'
        ' carácter de la cadena también debe estar en mayúscula, así como el'
        ' primer carácter no espacial después de un ".", "!" o "?" Por ejemplo,'
        ' si la función se proporciona con la cadena "¿a qué hora tengo que'
        ' estar allí? ¿cuál es la dirección?" entonces debería devolver la'
        ' cadena "¿A qué hora tengo que estar allí? ¿Cuál es la dirección?"')
string_1 = input("Ingrse una cadena de texto: \n\t")
print(f"Cadena sin capitalizar:\n\t{string_1}")  

string_2 = capitalizeStringV2(string_1)
print(f"Cadena capitalizada:\n\t{string_2}")
