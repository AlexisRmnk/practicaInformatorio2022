# Leer 2 números; si son iguales que los multiplique, si el primero 
# es mayor que el segundo que los reste y si no que los sume.

n1 = float(input("Ingrese el primer numero:\n"))
n2 = float(input("Ingrese el segundo numero:\n"))

if (n1 == n2):
    print(f"n1 == n2 >>>>> resultado = n1 * n2 = {n1*n2}")
elif(n1 > n2):
    print(f"n1 > n2 >>>>> resultado = n1 - n2 = {n1-n2}")
else:
    print(f"n1 + n2 = {n1+n2}")