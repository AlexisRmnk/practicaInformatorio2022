# encontrar todas las cifras de 3 digitos que cumplan con la condicion 
# de que la suma de los cubos de sus digitos sea igual al numero de la
# cifra que representa.
# ej: 153 
# 1**3 + 5 ** 3 + 3 ** 3 = 153

resultado = "Numero encontrados: "

for i in range(100,1000):
    centena = i//100
    decena_con_unidad = i%100
    decena = decena_con_unidad // 10
    unidad = decena_con_unidad % 10
    
    sumatoria_cubos_digitos = centena ** 3 + decena ** 3 + unidad ** 3
    if ( i == sumatoria_cubos_digitos ):
        resultado += f"{i} = {centena ** 3} + {decena ** 3} + {unidad ** 3}\n"
    
print(resultado)
    # print(f"Numero: {i}, centena = {centena}, decena con unidad ="
    # f" {decena_con_unidad}, decena = {decena}, unidad = {unidad}") 

    #version 2 en otro archivo! mas eficiente y para todos los rangos