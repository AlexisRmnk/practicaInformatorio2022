# tambien podemos usar un ALIAS para los tipos. Ej: listas anidadas de enteros
lista_enteros = list[int]
lista_anidada_2_niveles = list[lista_enteros]
def recibe_lista_anidada(lista_ani : lista_anidada_2_niveles):
    print(lista_ani)
    pass

lista_anid = [[1, 2, 3], [4, 5]]
recibe_lista_anidada(lista_anid)