#Ejercicio 7 : ¿Es un triángulo válido?                                 .
# Si tiene 3 varillas, posiblemente de diferentes longitudes, puede o no
#  ser posible colocarlas para que formen un triángulo cuando sus
#  extremos se toquen. Por ejemplo, si todas las varillas tienen una
#  longitud de 6 centímetros. entonces uno puede construir fácilmente
#  un triángulo equilátero con ellos. Sin embargo, si una varillas es
#  de 6 centímetros de largo, mientras que los otros dos son cada uno
#  de solo 2 centímetros de largo, entonces no se puede formar un
#  triángulo. En general, si una longitud es mayor o igual que la
#  suma de las otras dos, entonces las longitudes no pueden usarse
#  para formar un triángulo. De lo contrario, pueden formar un
#  triángulo. Escriba una función que determine si tres longitudes
#  pueden formar un triángulo. La función tomará 3 parámetros
#  y devolverá un resultado booleano. Además, escriba un programa
#  que lea 3 longitudes del usuario y muestre el comportamiento
#  de esta función.
def canMakeTriangle(len1, len2, len3):
    len1, len2, len3 = descendingOrder(len1, len2, len3)
    if len1 <= (len2 + len3):
        return True
    else:
        return False

def descendingOrder(n1, n2, n3):
    if (n1 > n2) and (n1 > n3):
        if (n2 > n3):
            (n1, n2, n3) = (n1, n2, n3)
        else:
            (n1, n2, n3) = (n1, n3, n2)
    elif(n2 > n1 and n2 > n3):
        if (n1 > n3):
            (n1, n2, n3) = (n2, n1, n3)
        else:
            (n1, n2, n3) = (n2, n3, n1)
    elif (n3 > n2 and n3 > n1):
        if (n2 > n1):
            (n1, n2, n3) = (n3, n2, n1)
        else:
            (n1, n2, n3) = (n3, n1, n2)
    elif (n1 == n2 and n3 > n1) or (n2 < n1 and n1 == n3): 
        (n1, n2, n3) = (n3, n1, n2)
    elif (n2 == n3 and n1 > n3) or (n1 == n2 and n3 < n1):
        (n1, n2, n3) = (n1, n2, n3)
    else: #numeros iguales
        (n1, n2, n3) = (n1, n2, n3)
    return (n1, n2, n3)

print("Ingrese 3 longitudes: ")
length_1 = float(input("Ingrese la longitud 1 en cm: \n\t"))
length_2 = float(input("Ingrese la longitud 2 en cm: \n\t"))
length_3 = float(input("Ingrese la longitud 3 en cm: \n\t"))

if canMakeTriangle(length_1, length_2, length_3):
    print(f"Un triangulo con lado 1 = {length_1} cm, lado 2 = ",end="")
    print(f"{length_2} cm y lado 3 = {length_3} cm es posible")
else:
    print(f"Un triangulo con lado 1 = {length_1} cm, lado 2 = ",end="")
    print(f"{length_2} cm y lado 3 = {length_3} cm es imposible")