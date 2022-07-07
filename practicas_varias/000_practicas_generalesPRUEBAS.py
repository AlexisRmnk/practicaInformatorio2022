def indet_posicion(*args):
    '''Imprime valores pasados por parametros'''
    for arg in args:
        print(arg)
        
lista_x1 = [1, 2,["a","b"], 4]
indet_posicion(*lista_x1)

def indet_nombre(**kwargs):
    '''Imprime valores pasados por parametros'''
    for key, value in kwargs.items():
        print(f"key: {key}, value: {value}")
        
diccionario_x1 = {"a":"A", "b": "B"}
indet_nombre(**diccionario_x1)