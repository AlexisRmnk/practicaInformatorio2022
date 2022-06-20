# botella PET - 1000 años
# bolsa de plastico - 150 años
# tetrabrik - 30 años
# chicle - 5 años

def prints_descomposition_time(type_material: int, type_dict: dict):
    print(f"{type_dict[type_material][0]} tarda {type_dict[type_material][1]}"
            " años en degradarse")