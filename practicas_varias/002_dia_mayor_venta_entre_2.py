ventas_d1 = int(input("Ingresar n° de ventas del dia 1: "))
ventas_d2 = int(input("Ingresar n° de ventas del dia 2: "))

if ventas_d1>ventas_d2:
    print("El dia 1 hubo mas ventas")
elif ventas_d2>ventas_d1:
    print("El dia 2 hubo mas ventas")
else:
    print("Los dos dias se vendio la misma cantidad de unidades.")

print(f"Detalle: El dia 1 se vendieron {ventas_d1} unidades mientras"
    f" que el dia 2 se vendieron {ventas_d2} unidades.")