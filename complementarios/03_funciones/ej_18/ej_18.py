# Ejercicio 18: Días en un mes
# Escriba una función que determine mostrar cuántos días hay en un mes en
#  particular. Su función tomará dos parámetros: el mes como un número
#  entero entre 1 y 12, y el año como un número entero de cuatro dígitos.
#  Asegúrese de que su función informa el número correcto de días en
#  febrero para los años bisiestos. Incluya un programa principal que
#  lea un mes y un año del usuario y muestre el número de días en ese mes.

# notas
# 31 dias:  enero (1), marzo(3), mayo(5), julio(7), agosto(8), octubre(10),
#           diciembre(12)
# 30 dias:  abril(4), junio(6), septiembre(9), noviembre(11), 
# 28 - 29 dias: febrero(12) (bisiesto c/4 años)
#   '00, '04 '08 ...

from def_ej_18 import *

i=1
month_names = ["Enero", "Febrero", "Marzo", "Abril", "Mayo",
                 "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
                 "Noviembre", "Diciembre"
              ]
while(True):
    print(f"\nIteracion {i}:")
    print(f"Ingrese un mes\t(0 para salir)")
    print("\t1) Enero\t7) Julio\n\t2) Febrero\t8) Agosto\n\t3) Marzo\t"
            "9) Septiembre\n\t4) Abril\t10) Octubre\n\t5) Mayo\t\t"
            "11) Noviembre\n\t6) Junio\t12) Diciembre")
    month = int(input("\n\t"))
    if month == 0:
        print("Finalizando ejecucion.")
        break
    elif month < 0 or month > 12:
        print("Valor incorrecto. Reintentar!")
        continue
    print("Ingrese un año (4 digitos, ej: 1998)")
    year = int(input("\t"))
    
    print(f"La cantidad de dias del mes {month_names[month-1]} en el año {year} es "
            f"{month_days(month, year)}.")
    i += 1