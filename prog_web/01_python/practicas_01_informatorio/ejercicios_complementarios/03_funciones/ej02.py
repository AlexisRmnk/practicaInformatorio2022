# En una jurisdicción particular, las tarifas de taxi consisten en una
#  tarifa base de $40.00, más $15.00 por cada 140 metros recorridos.
#  Escriba una función que tome la distancia recorrida (en kilómetros)
#  como su único parámetro y devuelva la tarifa total como su único
#  resultado. Escriba un programa principal que use la función.

# Sugerencia: Utilice constantes para presentar la base y la porción 
#  variable de las tarifas así el programa podrá actualizar fácilmente 
#  cuando las tasas aumentan.

def tarifa(mts):
    '''recibe distancia en metros como paramtro (float!)'''
    mts = round(mts, 2)
    base = 40
    x_metros = 140
    tarifa_por_x_metros = 15 #15 $ adicionales cada x_metros
    tarifa_total = base + (tarifa_por_x_metros * (mts/x_metros))
    tarifa_total = round(tarifa_total, 2)
    return(tarifa_total)


print("Ingrese cantidad de metros recorridos:")
metros = float(input("\t"))

print(f"Valor a pagar: ${tarifa(metros)}")