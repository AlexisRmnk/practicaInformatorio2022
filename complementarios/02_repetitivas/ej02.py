# Desarrollar una solución que calcule la suma de los cuadrados de los
# n primeros números naturales: 1 + 2**2 + 3**2 + … + n**2

n = int(input("Ingrese 'n'\n"))

texto = texto2 = ""
acumulador = 0
for num in range(1, n+1):
    acumulador = acumulador + num**2
    if (num != n):
        texto = texto + str(num) + "**2" + " + "
        texto2 = texto2 + str(num**2) + "   " + " + "
    else:
        texto = texto + str(num) + "**2"
        texto2 = texto2 + str(num**2)

print(f"Resultado final: {texto} = {acumulador}")
print(f"Resultado final: {texto2} = {acumulador}")