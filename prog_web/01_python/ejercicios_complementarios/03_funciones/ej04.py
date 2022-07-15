# Escriba una función que tome tres números como parámetros y devuelva
#  el valor medio de esos parámetros como resultado. Incluya un programa
#  principal que lea tres valores del usuario y muestre su mediana.

# Sugerencia: El valor medio es el medio de los tres valores cuando
#  se ordenan en orden ascendente. Se puede encontrar usando
#  declaraciones if, o con un poco de creatividad matemática.

def orden3NumsDescendiente(n1, n2 ,n3):
    # https://sites.google.com/view/complementarios/condicionales
    # Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.
    
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
    return n1, n2, n3

def orden3NumsAscendiente(n1, n2, n3):
    m1, m2, m3 = orden3NumsDescendiente(n1, n2, n3)
    return m3, m2, m1

def calcularMediana3Numeros(x1, x2, x3):
    x1, x2, x3 = orden3NumsAscendiente(x1, x2, x3)
    return x2

print("Ingrese 3 numeros para calcular el valor medio: ")
x1 = int(input("x1 = "))
x2 = int(input("x2 = "))
x3 = int(input("x3 = "))

mediana = calcularMediana3Numeros(x1, x2, x3)
print("La mediana es", mediana)