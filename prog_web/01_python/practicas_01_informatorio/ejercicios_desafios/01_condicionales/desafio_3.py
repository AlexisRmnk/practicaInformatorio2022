# Para el uso de fertilizantes es necesario medir cuánto abarca
# un determinado compuesto en el suelo el cual debe existir en una 
# cantidad de al menos 10% por hectárea, y no debe existir vegetación 
# del tipo MATORRAL. Escribir un programa que determine si es factible 
# la utilización de fertilizantes.

# 1 hectarea = 10.000 mts**2

m2_compuesto = float(input("Ingrese la cantidad del compuesto en el "
                            "suelo (en metros cuadrados): "))
hectareas = float(input("Ingrese la cantidad de hectareas del campo: "))
tipo_vegetacion = input("Ingrese el tipo de vegetacion presente: ")
tipo_vegetacion = tipo_vegetacion.upper()

m2_total = hectareas * 10000
porcentaje = m2_compuesto/m2_total * 100
porcentaje = round(porcentaje, 2)
print(f"Su tierra posee un {porcentaje}% de compuesto por hectarea. "
    f"Tipo de vegetacion presente: {tipo_vegetacion}")

if (porcentaje >= 10 and tipo_vegetacion != "MATORRAL"):
    print("Tierra apta para utilizacion de fertilizantes.")
else:
    print("Tierra no apta para utilizacion de fertilizantes.")