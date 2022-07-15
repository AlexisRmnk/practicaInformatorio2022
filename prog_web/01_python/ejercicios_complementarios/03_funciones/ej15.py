# Ejercicio 15: Verificar una contraseña

# En este ejercicio escribirá una función que determina si una
#  contraseña es buena o no. Definiremos como una buena contraseña
#  aquella que tenga una longitud de al menos 8 caracteres y contenga
#  al menos una letra mayúscula, al menos una letra minúscula y al menos
#  un número. Su función debe devolver verdadero si la contraseña que
#  se le pasó, como único parámetro, es buena, de lo contrario debería
#  devolver falso. Incluya un programa principal que lea una contraseña
#  del usuario e informe si es buena o no.

# metodos   (char).isupper() 
#           (char).islower()
# https://www.programiz.com/python-programming/methods/string/isdigit#:~:text=The%20isdigit()%20returns%20False,can%20use%20isnumeric()%20method.

def its_good_passw(passw):
    if len(passw) < 8:
        return False
    upper_case = lower_case = digit_ = False
    for char_ in passw:
        if char_.isupper():
            upper_case = True
        if char_.islower():
            lower_case = True
        if char_.isdigit():
            digit_ = True
    return (upper_case and lower_case and digit_)

while (True):
    print("Ingrese una contraseña para saber si es buena: (Definiremos como "
        "una buena contraseña aquella que tenga una longitud de al menos "
        "8 caracteres y contenga al menos una letra mayúscula, al menos una"
        " letra minúscula y al menos un número.) (Ingrese 0 para salir)")
    x_pass = input("\t")
    if x_pass == "0":
        break
    good = its_good_passw(x_pass)
    if good:
        print(f'La constaseña "{x_pass}" es buena!')
    else:
        print(f'La contraseña "{x_pass}" NO es buena.')
    print("\n")