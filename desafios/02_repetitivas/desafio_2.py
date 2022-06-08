# desafio 2
# https://sites.google.com/view/nivel1-desafios/repetitivas#h.8a580336l3dg

persona = 0
c_menos_100 = c_mas_100 = c_mas_200 = 0
while(True):
    persona += 1
    colillas = int(input(f"Ingrese la cantidad de colillas recolectadas"
    f" por la persona {persona} (escriba -1 para finalizar): "))
    if colillas == -1:
        persona = persona - 1
        break
    else:
        if colillas < 100:
            c_menos_100 += 1
        elif colillas >= 100 and colillas < 200:
            c_mas_100 += 1
        elif colillas >= 200:
            c_mas_200 += 1

print()
porc_c_menos_100 = round((c_menos_100/persona)*100, 2)
porc_c_mas_100 = round((c_mas_100/persona)*100, 2)
porc_c_mas_200 = round((c_mas_200/persona)*100, 2)
print(f"RESULTADOS.\nDe un total de {persona} personas:\n\t"
    f"{porc_c_menos_100}% junto menos de 100 colillas.\n\t"
    f"{porc_c_mas_100}% junto entre 100 y 199 colillas.\n\tEl restante "
    f"{porc_c_mas_200}% junto 200 colillas o mas.")

