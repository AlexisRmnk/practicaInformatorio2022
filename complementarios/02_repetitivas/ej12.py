# Calcular el monto a pagar por cada cliente y total recaudado en 
# una estación de servicio. Debe diseñar un programa que permita 
# monto por cliente y el total recaudado por la gasolinera, tomando
# en cuenta lo siguiente:

# • El precio del litro es para el Tipo A $50, para el Tipo B $ 55
#   y para el Tipo C $60

# • El programa finaliza cuando se introduce una D como tipo de gasolina.

client = 1
price = total = 0
while(True):
    print((f"\n\nIngrese datos de compra del cliente {client}:\t"))
    liters = float(input((f"Ingrese la cantidad de litros comprados:\n")))
    print((f"Ingrese el tipo de combustible comprado:\n"))
    print(f"'A' $50 ----- 'B' $55 ----- 'C' $60 ----- ('D' para SALIR)")
    tipe = input().upper()
    if tipe == "D":
        print("Finalizando programa.")
        client = client - 1
        break
    elif (tipe == 'A'):
        price = 50
    elif (tipe == 'B'):
        price = 55
    elif (tipe == 'C'):
        price = 60
    else:
        print("La letra no corresponde a los valores solicitados."
        " Reiniciando iteracion.\n")
        continue
    total_client = liters * price
    print(f"El cliente {client} debe abonar ${total_client} .")
    total = total + total_client
    client += 1

print(f"Se han cargado {client} clientes - ganancia total: ${total} .")
