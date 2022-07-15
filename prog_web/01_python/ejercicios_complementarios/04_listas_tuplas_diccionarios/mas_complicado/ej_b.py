# Leer una frase y luego invierta el orden de las palabras en la frase.
#  Por Ejemplo: “una imagen vale por mil palabras” debe convertirse en
#  “palabras mil por vale imagen una”.

while(True):
    string_ = input("Ingresar frase a invertir (0 para salir):\n\t")
    if string_ == "0":
        break
    string_ = string_.strip()
    list_ = string_.split()
    list_.reverse()
    tuple_ = tuple(list_)
    string_reversed = " ".join(tuple_) # string.join
    print(f"Frase invertida: \n\t{string_reversed}")