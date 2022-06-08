# https://sites.google.com/view/complementarios/condicionales
# Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.

print("Ingrese 3 numeros: ")
n1 = float(input("Ingrese el primer numero.\n"))
n2 = float(input("Ingrese el segundo numero.\n"))
n3 = float(input("Ingrese el tercer numero.\n"))

print("Numeros ordenados de mayor a menor:")
if (n1 > n2) and (n1 > n3):
    print(n1)
    if (n2 > n3):
        print(n2)
        print(n3)
    else:
        print(n3)
        print(n2)
elif(n2 > n1 and n2 > n3):
    print(n2)
    if (n1 > n3):
        print(n1)
        print(n3)
    else:
        print(n3)
        print(n1)
elif (n3 > n2 and n3 > n1):
    print(n3)
    if (n2 > n1):
        print(n2)
        print(n1)
    else:
        print(n1)
        print(n2)
elif (n1 == n2 and n3 > n1) or (n2 < n1 and n1 == n3): 
    print(n3)
    print(n1)
    print(n2)
elif (n2 == n3 and n1 > n3) or (n1 == n2 and n3 < n1) or ():
    print(n1)
    print(n2)
    print(n3)
else: #numeros iguales
    print(f"{n1} \t {n2} \t {n3}")