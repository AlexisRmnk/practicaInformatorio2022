
frutas = ["Manzana", "manzana", "PERA", "Pera", "pera", "Uva"]
# Convertimos todo a minúscula dentro del set comprehension
frutas_unicas = {f.lower() for f in frutas}
print(frutas_unicas)
list_frutas_unicas = list(frutas_unicas)
print(list_frutas_unicas)