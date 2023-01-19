# Un minorista en línea proporciona una forma de envío urgente de 
# $ 10.95 para el primer elemento y $ 2.95 para cada segundo elemento
#  posterior. Escriba una función que tome el número de elementos en
#  el pedido como su único parámetro. Devuelva los gastos de envío del
#  pedido como resultado de la función. Incluya un programa principal
#  que lea la cantidad de artículos comprados al usuario y muestre los
#  gastos de envío.


def gastosDeEnvio(elementos):
    if elementos < 0:
        print("ERROR - Cantidad de elementos ingresada negativa.")
        return -1
    if elementos == 0:
        return 0
    costoElemento1 = 10.95
    costoElementoExtra = 2.95
    elementos = elementos - 1
    return (costoElemento1) + elementos * costoElementoExtra


print("Ingrese el numero de elementos del pedido:")
x = int(input("\t"))
gasto = gastosDeEnvio(x)

if gasto != -1:
    print(f"El costo total para enviar {x} elementos es ${round(gasto, 2)}")
else:
    print("Fin de ejecucion de programa por excepcion.")