# https://sites.google.com/view/nivel1-desafios/funciones
# 150 años es el tiempo que tarda una bolsa de plástico común en degradarse
#  y una botella de PET puede tardar 1.000 años en desaparecer. 
# Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en
#  degradarse.
# Un trozo de chicle tarda 5 años en degradarse. 

# Se solicita una función para que dado el ingreso de un elemento,
#  se solicite tipo: Bolsa de plástico, botella PET, envase tetrabrik
#  o chicle, e imprima la cantidad de años que tarda en degradarse.
from def_desafio01 import prints_descomposition_time

dict_type_ = {1:["la bolsa de plastico", 150],
                2: ["la botella PET", 1000],
                3: ["el envase tetrabrik", 30],
                4: ["el chicle", 5]
             }

while(True):
    name_ = input("Ingrese nombre de elemento:\n\t")
    print("Ingrese tipo de elemento:")
    for key, value in dict_type_.items():
        print(f"\"{key}\" para {value[0]}", end=", ")
    print("\"0\" para salir.")
    type_ = int(input("\n\t"))
    if type_ == 0:
        print("FIN DE PROGRAMA")
        break
    elif type_ not in dict_type_.keys():
        print("Valor ingresado invalido - reiniciando consulta.")
        continue
    print(f"{name_}: ", end="")
    prints_descomposition_time(type_, dict_type_)

        