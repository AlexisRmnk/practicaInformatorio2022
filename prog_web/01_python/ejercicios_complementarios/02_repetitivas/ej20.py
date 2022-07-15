# El Centro de Salud de Rosario tiene registradas N consultas médicas de
#  menores. De cada consulta tiene como datos: la edad del menor y el 
#  día de visita. Los datos están ordenados en forma creciente por día.
# Proponer un fin de datos para cada día. Se desea conocer, para cada día,
#  la edad promedio de pacientes y además el día en que se registró el 
#  máximo de pacientes.

edad_acum = paciente_maximo = 0
dia = paciente = 1

while(True):
    print(f"DIA {dia}")
    while(True):
        print(f"Ingresar datos del paciente {paciente}.")
        edad = int(input("Ingresar la edad (en años):\n\t"))
        edad_acum = edad_acum + edad
        x = input("Desea ingresar mas pacientes?\tS (Si) / N (NO):\n\t").upper()
        if (x == "S" or x == ""):
            paciente += 1
        elif(x == "N"):
            break
        else:
            print("Caracter no valido, reiniciando iteracion.")
    
    edad_promedio = round(edad_acum / paciente, 2)
    print(f"EDAD PROMEDIO DE PACIENTES PARA EL DIA {dia}: "
            f"{edad_promedio} años.")
    
    if (paciente > paciente_maximo):
        paciente_maximo = paciente
        dia_maximo = dia

    paciente = 1
    edad_acum = 0
    y = input("Desea ingresar mas dias?\tS (Si) / N (NO):\n\t").upper()
    if (y == "S" or y == ""):
        dia += 1
    elif(y == "N"):
        break
    else:
        print("Caracter no valido, reiniciando iteracion.")

print(f"El dia que se registro mas pacientes fue el dia {dia_maximo}"
        f" con {paciente_maximo} pacientes registrados.")