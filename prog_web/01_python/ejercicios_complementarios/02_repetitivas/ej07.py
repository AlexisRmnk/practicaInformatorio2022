# Realizar un programa que calcule y muestre la suma de los múltiplos
#  de 5 comprendidos entre dos valores A y B. El programa no permitirá
#  introducir valores negativos para A y B y verificará que A es menor
#  que B. Si A es mayor que B, se deben intercambiar los valores.

while True:
    a = int(input("Introduce un numero entero positivo:\n"))
    b = int(input("Introduce otro numero entero positivo:\n"))
    if (a >= 0 and b >= 0):
        break
    else:
        print("Se introdujo un valor negativo. Reintentar!\n")

#print("test 1: a vale ", a, " y b vale ", b)

if (a > b):
    (a, b) = (b, a) #intercambia valores!

#print("test 2: a vale ", a, " y b vale ", b)
print("\n", end="")

contador = acumulador = 0
for i in range(a, b+1, 1):
    if (i%5 == 0):
        print(f"{i} es multiplo de 5")
        acumulador = acumulador + i
        contador += 1

print(f"\nLa suma de los {contador} multiplos de 5 comprendidos entre"
        f" {a} y {b} vale {acumulador}")
