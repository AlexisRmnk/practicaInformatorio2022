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
    
    def sum_products_price(self, ask_brand = False):
        sum_ = 0
        if ask_brand:            
            brand = input("Especificar marca:\n\t").title().strip()
            string_ = ""
            for p in self.products:
                if p.getBrand() == brand:
                    sum_ = sum_ + p.getPrice()
                    string_ = string_ + p.return_str_atts() + "\n"
            print(f"La suma de precios de los {len(self.products)} productos "
                f"de la marca {brand} es: $ {sum_}")
            print(f"Los mismos se listan a continuacion: {string_}")
        else:
            for p in self.products:
                sum_ = sum_ + p.getPrice()
            print(f"La suma de precios de los {len(self.products)} productos "
                f"es: $ {sum_}")
           
    
    def sort_by_id(self):
        ''' 
        Sorts an list of products by the first key value ("id" in this case).
        '''
        def returns_id_value(product_):
            return (product_.getId_())
        
        self.products.sort(key = returns_id_value)
        # https://docs.python.org/3/howto/sorting.html#:~:text=sort()%20and%20sorted(),element%20prior%20to%20making%20comparisons.&text=The%20value%20of%20the%20key,to%20use%20for%20sorting%20purposes. 
    
    
    def add_product(self): 
        print("AGREGAR PRODUCTO:\nIndicar tipo de producto:")
        print("\t1) Agua Mineral\n\t2) Gaseosa")
        x = personal_functions.check_return_int(input("\t"))
        x = personal_functions.check_range(x, 1, 2) # returns 1 or 2
        if x == 1:
            p = MineralWater()
            id_ = self.__checksId(p.getId_()) # id_
            p.setId_(id_)   
        else:
            p = Soda()
            id_ = self.__checksId(p.getId_()) # id_
            p.setId_(id_)
        self.products.append(p)

    def del_product(self):
        print("Introducir la ID del producto a borrar: ")
        id_x = input("\t")
        for p in self.products:
            if id_x == p.getId_():
                print(p.return_str_atts())               
                print("Confirmar eliminacion de producto (0 - NO, 1 - SI)")
                x = personal_functions.check_return_int(input("\t"))
                x = personal_functions.check_range(x, 0, 1)
                if x == 1:
                    self.products.remove(p)
                    print("Producto eliminado exitosamente.")
                    return
        print("ID no encontrada. No se eliminaron registros.")

    def show_products(self):
        self.sort_by_id()
        for p in self.products:
            print(p.return_str_atts())

    def getProducts(self):
        return self.products
    def setProducts(self, products):
        self.products = products

class Product:
    def __init__(self):
        print("Ingresar datos:")
        self.id_ = input("Id: ").upper().strip()
        self.liters = input("Litros: ")
        self.price = personal_functions.check_return_float(input("Precio: $ "))
        self.brand = input("Marca: ").title().strip()
    
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
    def __init__(self):
        super().__init__()
        self.origin = input("Origen: ")
    
    def return_str_atts(self):
        return (super().return_str_atts() + f", Origen: {self.origin}")
        
    def getOrigin(self):
        return self.origin
    def setOrigin(self, origin):
        self.origin = origin

class Soda(Product):
    def __init__(self):
        super().__init__()
        self.p_sugar = input("Porcentaje de azucar: ")
        x = personal_functions.check_return_int(input("Tiene promocion? "
                                                      "(0 - NO, 1 - SI)\n\t"))
        x = personal_functions.check_range(x, 0, 1)
        has_promo = bool(x)
        self.has_promo = has_promo
        if has_promo:
            self.price = self.price - self.price*0.1  

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