# simular cajero super - user compra 3 productos - ingresar cantidad de
# prodcts que compro y hay que devolver el monto #  total a pagar del
# usuario (agregandole el iva de 21%)

# El usuario compra tres productos - Ingresa la cantidad de cada producto 
# que compro - calcular el monto total del usuario + iva

print("Programa clase 2 - compra de procutos en supermercado",
        "con iva de 21%")
        # input devuelve un string que hay que pasar a entero
n_prod = int(input("Ingrese cantidad de focos que compra: ")) 
precio = float(input("Ingrese precio de focos: "))

n_prod2 = int(input("Ingrese cantidad de cables que compra: "))
precio2 = float(input("Precio de cables: "))

n_prod3 = int(input("Ingrese cantidad de bulones que compra: "))
precio3 = float(input("Precio de bulones: "))

iva = 21

total = (((n_prod * precio) + (n_prod2 * precio2) + (n_prod3 * precio3)) 
        * ((100 + iva)/100))
print(f"Su total es de ${total}. Detalle: numero de productos: 3, ",
        f" iva: {iva}%")

test = (2 
+ 2)
print(test)


