#DADO EL MONTO DE COMPRA DE UN CLIENTE
#si LA COMPRA es MAYOR A #10000 DESCONTAR 5%
#si la compra es mayor a 15000 descontar 10%
#si la compra es mayor a 50000 descontar un 20%
#si la compra es mayor a 100000 descontar un 30%
# MOSTRAR AL FINAL EL MONTO TOTAL Y EL DESCUENTO REALIZADO

compra = float(input("Ingrese el valor de la compra: $"))
compra_inicial = compra

if (compra > 100000):
    descuento = compra * 0.3
    compra = compra - (descuento)
elif (compra > 50000):
    descuento = compra * 0.2
    compra = compra - (descuento)
elif (compra > 15000):
    descuento = compra * 0.1
    compra = compra - (descuento)
elif (compra > 10000):
    descuento = compra * 0.05
    compra = compra - (descuento)
else:
    descuento = 0

print(f"Monto inicial: ${compra_inicial}")
print(f"Descuento: ${round(descuento, 2)}")
print(f"Monto final: ${round(compra, 2)}")
