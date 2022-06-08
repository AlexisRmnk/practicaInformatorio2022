# Un censador recopila ciertos datos aplicando encuestas para el último
# Censo Nacional de Población y Vivienda. Desea obtener de todas las
# personas que alcance a encuestar en un día, que porcentaje tiene
# estudios de primaria, secundaria, carrera técnica, estudios profesionales
# y estudios de posgrado.

ninguno = primaria = secundaria = tecnica = profesionales = posgrado = 0
persona = 1
while(True):
    print("\n///////////////////////////////////////////////////////\n")
    print(f"Ingrese el nivel de estudios terminados de la persona " 
        f"{persona}:\n(0 - sin estudios\n"
        f" 1 - estudios de primaria\n 2 - estudios de "
        "secundaria\n 3 - carrera tecnica\n 4 - estudios profesionales"
        " (universitarios)\n 5 - estudios de posgrado)\n\n"
        "Ingrese x (equis) para salir.")
    estudios = input().lower()
    if (estudios == "x"):
        persona = persona - 1
        break
    elif (estudios == "0"):
        print(f"Sin estudios terminados, seleccionado para la persona"
                f" {persona}")
        ninguno += 1
    elif (estudios == "1"):
        print(f"Estudios de primaria seleccionado para la persona"
                f" {persona}")
        primaria += 1
    elif(estudios == "2"):
        print(f"Estudios de secundaria seleccionado para la persona"
                f" {persona}")
        secundaria += 1
    elif(estudios == "3"):
        print(f"Estudios de carrera tecnica seleccionado para la persona"
                f" {persona}")
        tecnica += 1
    elif(estudios == "4"):
        print(f"Estudios profesionales (universitarios) seleccionado "
                f"para la persona {persona}")
        profesionales += 1
    elif(estudios == "5"):
        print(f"Estudios de posgrado seleccionado para la persona"
                f" {persona}")
        posgrado += 1
    else:
        print("Seleccion erronea. Reintentar")
        continue
    persona += 1

print(f"Total de personas: {persona}")
print(f"{ninguno} personas (el {round((ninguno/persona) * 100, 2)}%)"
        " no posee estudios.")
print(f"{primaria} personas (el {round((primaria/persona) * 100, 2)}%)"
        " tiene estudios de primaria.")
print(f"{secundaria} personas (el {round((secundaria/persona) * 100, 2)}%)"
        " tiene estudios de secundaria.")
print(f"{tecnica} personas (el {round((tecnica/persona) * 100, 2)}%)"
        " tiene estudios de carrera tecnica.")
print(f"{profesionales} personas (el {round((profesionales/persona) * 100, 2)}"
        "%) tiene estudios profesionales.")
print(f"{posgrado} personas (el {round((posgrado/persona) * 100, 2)}%)"
        " tiene estudios de posgrado.")