# Para seguir colaborando en esta misión de salvar al planeta, 
# necesitamos que elabores un programa en Python que dado el 
# tamaño de un pez indique si su organismo está contaminado. 
# Para ello tendremos 4 opciones:

# Tamaño Normal: Mensaje "Pez en buenas condiciones".
# Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de
# nutrición".
# Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas
# de organismo contaminado".
# Tamaño sobredimensionado: Mensaje "Pez contaminado"

print("\nBienvenido. Indique el tamaño de un pez para determinar si el "
        "agua está contaminada\n")

size = int(input("Ingrese:\n\t'1' si el pez presenta un tamaño normal. \n\t'2' "
                    "si el pez presenta un tamaño por debajo de lo "
                    "normal. \n\t'3' si presenta un tamaño un poco por "
                    "encima de lo normal. \n\t'4' si el pez posee un "
                    "tamaño sobredimensionado (muy grande)."))
if(size == 1):
    print("Pez en buenas condiciones.")
elif(size == 2):
    print("Pez con problemas de nutrición.")
elif(size == 3):
    print("Pez con síntomas de organismo contaminado.")
elif(size == 4):
    print("Pez contaminado.")
else:
    print("No se escribió un dígito valido.")