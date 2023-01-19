# Determinar el número mayor de 10 números ingresados.

maxim = 0
for num in range(1,11):
    x = float(input(f"Iteracion {num}. Ingrese un numero:\n"))
    if (x > maxim):
        maxim = x
        
print("El numero mayor de los 10 numeros ingresados es el ", maxim)