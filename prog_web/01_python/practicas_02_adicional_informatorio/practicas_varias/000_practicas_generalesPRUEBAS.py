class Producto: # si el nombre fuera mas largo se podria usar ProductoPrincipal,
                # por ejemplo

    # metodo constructor, siempre se ejecuta al crear el objeto
    # los metodos son esencialmente funciones dentro de objetos
    # aplican las mismas reglas (valores por defecto, etc)
    def __init__(self, nombre, precio : float, stock = 0):
        'Crea una instancia de producto'
        self.name = nombre
        self.price = precio
        self.stock = stock
        self.marca = "Marca por defecto" 
    
    # metodos
    def mostrar_nombre(self):
        print(f"Nombre del producto: {self.name}")

    def mostrar_stock(self):
        print(f"Stock del producto: {self.stock}")
    
    def modificar_stock(self, nuevo_stock):
        self.stock = nuevo_stock

    def devolver_stock(self):
        return self.stock
    
    def mostrar_todo(self):
        self.mostrar_nombre()
        print(f'Precio: $ {self.price}')
        self.mostrar_stock()
        print(f'Marca: {self.marca}', end='\n\n')


producto1 = Producto("Tornillo", 23.5, 5)


# Ejemplo con Clase definida mas arriba
print('producto1.__dict__: \n',producto1.__dict__) # imprime diccionario de atributos
print('producto1.__dir__(): \n',producto1.__dir__()) # imprime lista con todos los metodos

