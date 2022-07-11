def catalogar1(vehiculos_:list):
    for obj_vehiculo in vehiculos_:
        print(f"Tipo de vehiculo: {type(obj_vehiculo).__name__}. Atributos:")
        print(obj_vehiculo.getValores())

def catalogar2(vehiculos_:list, ruedas = None):
    if ruedas == None:
        for obj_vehiculo in vehiculos_:
            print(f"Tipo de vehiculo: {type(obj_vehiculo).__name__}."
                  " Atributos:")
            print(obj_vehiculo.getValores())
    else:
        contador = 0
        for obj_vehiculo in vehiculos_:
            if ruedas == obj_vehiculo.getRuedas():
                contador += 1
                print(f"Tipo de vehiculo: {type(obj_vehiculo).__name__}. "
                      "Atributos:")
                print(obj_vehiculo.getValores())
        print(f"Se han mostrado {contador} vehiculos con {ruedas} ruedas.")