# encontrar todas las cifras de 3 digitos que cumplan con la condicion 
# de que la suma de los cubos de sus digitos sea igual al numero de la
# cifra que representa.
# ej: 153 
# 1**3 + 5 ** 3 + 3 ** 3 = 153

for i in range(100,1000):
    string = str(i)
    suma = 0
    for digito in string:
        suma = suma + (int(digito) ** 3)
    if i == suma:
        print(i)