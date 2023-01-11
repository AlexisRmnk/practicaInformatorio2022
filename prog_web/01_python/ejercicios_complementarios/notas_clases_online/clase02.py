
from re import A
from this import d


print("Inicio prueba diccionario")
# diccionario
diccionarioTest = {
    "Y": "ypsilon" ,
    "cadena": "valor cadena",
    True: "valor true",
    False: "valor false",
    1: "uno",
    "dos": 2
}
print("Nuestro diccionario es de tipo: ", type(diccionarioTest), 
", visto con el comando type(variable)")

print('diccionarioTest["Y"]', diccionarioTest["Y"])
print('diccionarioTest["cadena"]', diccionarioTest["cadena"])
print('diccionarioTest[True]', diccionarioTest[True])
print('diccionarioTest[False]', diccionarioTest[False])
print('diccionarioTest[1]', diccionarioTest[1])
print('diccionarioTest["dos"]', diccionarioTest["dos"])

print("(Con comillas simples) diccionarioTest['dos']", diccionarioTest["dos"])

print("Fin prueba diccionario")


x=123
y="_cadena_de_texto_"
print(f"test nuevo print {x} - {y}") #notar la "f" al principio del string
print("test nuevo print {x} - {y}")


