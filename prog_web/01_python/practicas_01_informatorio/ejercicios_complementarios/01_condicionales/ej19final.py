# Una distribuidora de libros vende a librerías y a particulares. 
# Aplica bonificaciones por cantidad según el siguiente criterio:
#     i.    a librerías:    hasta 24 unidades, el 20%; 
#                           más de 24 unidades, el 25%.
#     ii.   a particulares: menos de 6 unidades, nada; 
#                           desde 6 hasta 18 unidades, el 5% y 
#                           más de 18 unidades, el 10%.

# El tipo de cliente está codificado así: 'L' para librerías, 'P' para 
# particular. Dado el importe bruto de una compra de libros, el tipo de
# cliente de que se trata y la cantidad total pedida por el mismo, 
# determinar el importe bruto bonificado.


cant = int(input("Ingrese cantidad de unidades compradas:\n"))
bruto = float(input("Ingrese el importe total de la compra:\n"))
tipo = input("Ingrese el tipo de cliente ('L' para librerias, 'P' para"
            " particular):\n").upper()

if tipo == "L":
    if(cant > 24):
        porc_bonif = 0.25
    else:
        porc_bonif = 0.20
elif tipo == "P":
    if(cant < 6):
        porc_bonif = 0
    elif(6 <= cant <= 18):
        porc_bonif = 0.05
    else:
        porc_bonif = 0.1
else: 
    print("El tipo introducido es incorrecto.")
    exit()

importe_bonif = bruto - (bruto * porc_bonif)
print(f"Importe bruto bonificado (% {porc_bonif*100} de descuento) "
        f"= {importe_bonif}")