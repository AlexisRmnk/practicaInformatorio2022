# Crea un diccionario donde la clave sea el nombre de biólogos y el valor
#  sea el email (no es necesario validar). Tendrás que ir pidiendo
#  contactos hasta el usuario diga que no quiere insertar mas. No se
#  podrán insertar nombres repetidos.

dictionary_ = dict()
i = 1

while(True):
    
    print(f"Iteracion {i}:")
    print("Ingrese el nombre de biologo/a. (0 para salir)"
            " (1 para mostrar lista de nombres/emails actual)")
    name_ = input("\t")
    name_ = name_.capitalize()
    if name_ == "0":
        print(f"Estado final de diccionario: {dictionary_}")
        break
    elif name_ == "1":
        print(f"Estado actual del diccionario: {dictionary_}")
        continue
    elif name_ in dictionary_.keys():
        print("Ese nombre ya se encuentra en uso! Reintentar!")
        continue
    
    print(f"Ingrese el email del biologo/a \"{name_}\":")
    email_ = input("\t")
    dictionary_[name_] = email_
    i += 1
    