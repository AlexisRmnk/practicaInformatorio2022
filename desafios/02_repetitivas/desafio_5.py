# desafio 5
# https://sites.google.com/view/nivel1-desafios/repetitivas#h.s6nhipu2ug9k

cant_basura = cant_basura_multados = vehiculo = 0
while(True):
    vehiculo += 1
    codigo = ""
    x = input("Desea generar el codigo de vehiculo o ya posee codigo? "
                "Presione cualquier tecla para generar codigo. "
                "Presione 'N' si ya posee el codigo.\n").upper()
    if (x == 'N'): # ya posee codigo
        print("Se indico que ya se posee el codigo. \n"
                f"Ingrese el codigo del vehiculo {vehiculo}"
                " a continuacion. Primero se solicitaran las 3"
                " letras iniciales y luego los 5 digitos finales.\n")
        codigo_letras = input("Ingrese 3 letras iniciales:"
                                " (EJ: AAA)\n").upper()
        codigo_numero = input("Ingrese valor numerico de 5 digitos:"
                                    " (EJ: 33300\n")
        codigo = codigo_letras + codigo_numero
        print(f"CODIGO: {codigo}")
    else:
        print("Se generara un codigo nuevo.")
        patente = input(f"Ingrese la patente del vehiculo {vehiculo}. (3" 
                    " letras y 3 numeros. Todo de corrido."
                    " Ej: AAA333\n").upper()
        basura = input(f"El vehiculo de patente {patente},"
                            f"tiro basura en la via publica? "
                            f"('1' para SI. '0' para NO)\n")
        #basura_b = bool(basura)
        multas = input(f"El vehiculo de patente {patente},"
                            f"fue multado previamente? "
                            f"('1' para SI. '0' para NO)\n")
        #multas_b = bool(multas)
        codigo = patente + basura + multas
        print(f"CODIGO GENERADO: {codigo}")
    # en este punto ya tenemos el codigo ej. AA33300
    if (codigo[6] == "1"):
        cant_basura += 1
        if (codigo[7] == "1"):
            cant_basura_multados += 1
            
    salir = input(f"Agregar otro vehiculo? N° de vehiculos agregados: "
                    f"{vehiculo}. ('N' para Salir)").upper()
    if (salir == "N"):
        break
print("\nANALISIS DE RESULTADOS:\n")

print(f"Cantidad de vehiculos observados: \t{vehiculo}.\nCantidad de "
        f"vehiculos que han tirado basura: \t{cant_basura}.\nPorcentaje"
        f" de vehiculos que tiraron basura y ya habian sido multados"
        f" previamente: \t{round((cant_basura_multados/cant_basura)*100, 2)}.")