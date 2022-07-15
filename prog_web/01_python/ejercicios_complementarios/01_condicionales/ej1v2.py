# https://sites.google.com/view/complementarios/condicionales
# Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.

print("Ingrese 3 numeros: ")
n1 = float(input("Ingrese el primer numero.\n"))
n2 = float(input("Ingrese el segundo numero.\n"))
n3 = float(input("Ingrese el tercer numero.\n"))

print("Numeros ordenados de mayor a menor:")
if (n1 > n2 > n3):
    print(n1)
    print(n2)
    print(n3)
elif(n2 > n3 > n1):
    print(n2)
    print(n3)
    print(n1)
elif(n2 > n1 > n3):
    print(n2)
    print(n1)
    print(n3)
elif(n1 > n3 > n2):
    print(n2)
    print(n3)
    print(n1)
elif(n3 > n1 > n2):
    print(n3)
    print(n1)
    print(n2)
else:
    print(n3)
    print(n2)
    print(n1)