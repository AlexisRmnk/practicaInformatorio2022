# Bebidas online
# https://sites.google.com/view/informatorio-poo/level-stone/level-stone#h.ufgbj5fz9rdk

# WIP

# This block of code is for using my own functions
# https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
# https://www.codegrepper.com/code-examples/python/python+call+function+from+another+folder
import sys # sys.path is a list of absolute path strings
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.parent.parent.resolve()))
# check number of ".parent" using
# print(str(pathlib.Path(__file__).parent.parent.parent.parent.parent.resolve()))
# it has to return something like "...\prog_web\01_python"
import personal_functions
# print(personal_functions.test())


class Deposit:
    def __init__(self) -> None:
        self.products = list() #products = drinks
    
    def __checksId(self, id_):
        '''Checks if the id isnt on another product'''
        while(True):
            flag = False
            for p in self.products:
                if p.getId_() == id_:
                    flag = True
                    break
            if flag:
                print(f"La identificacion {id_} ya existe, probar otro "
                        "valor!")
                id_ = input("\t")
            else:
                break
        return id_
    
    def add_product(self): 
        print("AGREGAR PRODUCTO:\nIndicar tipo de producto:")
        print("\t1) Agua Mineral\n\t2) Gaseosa")
        x = personal_functions.check_return_int(input("\t"))
        x = personal_functions.check_range(x, 1, 2) # returns 1 or 2
        if x == 1:
            p = MineralWater()
            tuple_ = p.asks_info()
            list_ = list(tuple_)
            list_[0] = self.__checksId(list_[0]) # id_
            tuple_ = tuple(list_)
            p = MineralWater(tuple_)   
        else:
            p = Soda()
            tuple_ = p.asks_info()
            list_ = list(tuple_)
            list_[0] = self.__checksId(list_[0]) # id_
            tuple_ = tuple(list_)
            p = Soda(tuple_)
        self.products.append(p)

    def show_products(self):
        for p in self.products:
            print(p.return_str_atts())

    def getProducts(self):
        return self.products
    def setProducts(self, products):
        self.products = products

class Product:
    def __init__(self, id_="", liters=0, price=0, brand=""):
        self.id_ = id_
        self.liters = liters
        self.price = price
        self.brand = brand
    
    def asks_info(self):
        print("Ingresar datos:")
        id_ = input("Id: ")
        liters = input("Litros: ")
        price = input("Precio: $ ")
        brand = input("Marca: ")
        return id_, liters, price, brand
    
    def return_str_atts(self):
        return(f"ID: {self.id_}, litros: {self.liters}, precio: "
                 f"$ {self.price}, marca: {self.brand}")
    
    def getId_(self):
        return self.id_
    def setId_(self, id_):
        self.id_ = id_
    def getLiters(self):
        return self.liters
    def setLiters(self, liters):
        self.liters = liters
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getBrand(self):
        return self.brand
    def setBrand(self, brand):
        self.brand = brand
    
class MineralWater(Product):
    def __init__(self, id_="", liters=0, price=0, brand="", origin=""):
        super().__init__(id_, liters, price, brand)
        self.origin = origin   
        
    def asks_info(self):
        id_, liters, price, brand = super().asks_info()
        origin = input("Origen: ")
        return id_, liters, price, brand, origin
    
    def return_str_atts(self):
        return (super().return_str_atts() + f", Origen: {self.origin}")
        
    def getOrigin(self):
        return self.origin
    def setOrigin(self, origin):
        self.origin = origin
        
    

class Soda(Product):
    def __init__(self, id_="", liters=0, price=0, brand="", p_sugar=0, 
                 has_promo=False):
        super().__init__(id_, liters, price, brand)
        self.p_sugar = p_sugar
        self.has_promo = has_promo
        if has_promo:
            self.price = price - price*0.1
        
    def asks_info(self):
        id_, liters, price, brand = super().asks_info()
        p_sugar = input("Porcentaje de azucar: ")
        x = personal_functions.check_return_int(input("Tiene promocion? "
                                                      "(0 - NO, 1 - SI)"))
        x = personal_functions.check_range(x, 0, 1)
        has_promo = bool(x)
        return id_, liters, price, brand, p_sugar, has_promo  

    def return_str_atts(self):
        string_ = (super().return_str_atts() + f", Porcentaje de azucar:"
                f" {self.p_sugar}, Tiene promocion del 10% incluida en el "
                "precio: ")
        if self.has_promo:
            string_ = string_ + "SI"
        else:
            string_ = string_ + "NO"
        return string_
    
    def getP_sugar(self):
        return self.p_sugar
    def setP_sugar(self, p_sugar):
        self.p_sugar = p_sugar
    def getHas_promo(self):
        return self.has_promo
    def setHas_promo(self, has_promo):
        self.has_promo = has_promo    




def menu():
    d = Deposit()
    while(True):
        op = personal_functions.make_menu("Agregar producto",
            "Eliminar producto",
            "Mostrar informacion",
            "Calcular precio de todas las bebidas",
            "Calcular el precio total de una marca de bebida",
            exit_option = "Salir"        )
        if op == 0:
            print("Finalizando ejecucion.")
            break
        elif op == 1:
            d.add_product()
        elif op == 2:
            pass
        elif op == 3:
            d.show_products()
        elif op == 4:
            pass
        else: # op = 5
            pass




# MAIN
menu()