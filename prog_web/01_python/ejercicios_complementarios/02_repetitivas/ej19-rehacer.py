# Dados los datos de un municipio: zona, sexo y edad de cada uno de
#   sus habitantes, encontrar:

# a) porcentaje de varones menores de 15 años para cada zona

# b) porcentaje de varones menores de 15 años para todo el municipio

# Los datos vienen ordenados por zona. Con dato de zona igual a 0, se indica
#   el fin
contador = 1
municipio = zona_1 = zona_2 = zona_3 = 0

while(True):
    print(f"HABITANTE N° {contador}:")
    zona = int(input("Ingrese zona (de 1 a 3 - Envie 0 para salir):\n\t"))

    if (zona == 0):
        print()
        break
    print("Ingrese sexo ('M' para masculino / 'F' para femenino):")
    sexo = input("\t").upper()

    if (sexo != 'M' and sexo != 'F'):
        print("ERROR - Sexo ingresado invalido. Reiniciando cuestionario.")
        continue
    if (zona < 0 or zona > 3):
        print("ERROR - Zona ingresada invalida. Reiniciando cuestionario.")
        continue

    print("Ingrese edad (en años):")
    edad = int(input("\t"))

    if edad < 15 and sexo == "M":
        municipio += 1
        if zona == 1:
            zona_1 += 1
        elif zona == 2:
            zona_2 += 1
        elif zona == 3:
            zona_3 += 1
    contador += 1
    
porc_z1 = round((zona_1/municipio) * 100, 2)
porc_z2 = round((zona_2/municipio) * 100, 2)
porc_z3 = round((zona_3/municipio) * 100, 2)

print("Porcentajes de varones menores de 15 años para cada zona:")
print(f"Zona 1: {porc_z1} % ({zona_1} habitantes).")
print(f"Zona 2: {porc_z2} % ({zona_2} habitantes).")
print(f"Zona 3: {porc_z3} % ({zona_3} habitantes).")

print("\nPorcentaje de varones menores de 15 años para todo el municipio:"
        f" {round((municipio/contador)*100, 2)} % ({municipio} de "
        f"{contador} habitantes).")