
'''lista_1 = ['gato','perro','hipopotamo','cebra','saltamontes']

lista_nombres_cortos1 = [animal for animal in lista_1 if len(animal) <= 5]

print(lista_nombres_cortos1)

lista_nombres_cortos2 = [animal  for animal in lista_1 ]

print(lista_nombres_cortos2)'''

numeros = [1, 2, 3]
etiquetas = [("Par" if n % 2 == 0 else "Impar") for n in numeros]
print(etiquetas)