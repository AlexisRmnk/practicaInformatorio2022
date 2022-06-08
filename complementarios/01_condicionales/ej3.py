# Determinar si el primero de un conjunto 
# de tres números dados, es menor que los otros dos.

print("Ingrese 3 numeros: ")
n1 = float(input("Ingrese el primer numero.\n"))
n2 = float(input("Ingrese el segundo numero.\n"))
n3 = float(input("Ingrese el tercer numero.\n"))

if (n1 < n2 and n1 < n3):
    print(f"El numero {n1} es menor que los numeros {n2} y {n3}.")
else:
    print(f"El numero {n1} NO es menor que los numeros {n2} y {n3}.")