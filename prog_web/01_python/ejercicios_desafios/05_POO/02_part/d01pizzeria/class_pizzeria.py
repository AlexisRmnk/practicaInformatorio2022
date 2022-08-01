import datetime
import random

from def2_pizzeria import *

class Pizzeria:
    def __init__(self) -> None:
        self.orders = list() #type: list[Order]
        
        #tipo : list[variety]
        self.varieties_menu = self.__generate_varieties_menu()
        
    
    def __generate_varieties_menu(self):
        var1={"name":"Mozzarella", "price":50, "ingredients":[
            "Queso mozzarella","Tomate","Huevo"
        ]}
        var2={"name":"Fugazza", "price":60, "ingredients":[
            "Queso mozzarella","Cebolla","Huevo"
        ]}
        var3={"name":"Mozzarella con champiniones", "price":55, "ingredients":[
            "Queso mozzarella","Tomate","Huevo","Champiniones"
        ]}
        vars = [var1, var2, var3]
        varieties_menu = list()
        enumeration = 1
        for var_x in vars:
            for size_n in range(3):
                for type_n in range(3):
                    new_var = Variety(enumeration, var_x["name"], var_x["price"], 
                                       size_n, type_n, var_x["ingredients"])
                    enumeration = enumeration + 1
                    varieties_menu.append(new_var)
        return varieties_menu
                    
    def modify_orders_date(self):
        '''Modifies dates on orders by subtracting 1 to 30 days randomly'''
        print("Esta seguro que desea modificar las fechas? (S/N)"
              "ACCION NO REVERSIBLE")
        answ_ = return_S_N()
        if answ_ == "S":
            for order in self.orders:
                date_1 = order.getDelivered_date()
                date_1_mod = date_1 - datetime.timedelta(
                    days= random.randint(1, 30)) 
                date_1_mod_str = date_1_mod.strftime('%d/%m/%Y %H:%M:%S')
                order.setDelivered_date(date_1_mod)
                order.setDelivered_date_str(date_1_mod_str)
        else:
            print("Accion abortada.")        
                
    def generate_order(self):
        order = Order(self.varieties_menu)
        self.orders.append(order)

    def show_orders(self):
        i=0
        for order in self.orders:
            i+=1
            print("-"*50)
            print(f"--- Pedido N°{i} " + "-"*30)
            print(order)
            print("-"*50)

    def __get_y_m_d(self):
        '''Asks and returns a date'''
        print("Año:")
        year = check_range(check_non_negative_int(
            convert_to_int(input("\t"))), 1900, 2100)
        print("Mes:")
        month = check_range(check_non_negative_int(
            convert_to_int(input("\t"))), 1, 12)
        max_day = month_days(month, year)
        print("Dia:")
        day = check_range(check_non_negative_int(
            convert_to_int(input("\t"))), 1, max_day) #type: ignore
        return datetime.date(year, month, day)
        
    def income_period(self): 
        '''Prints income and detail for a given period'''
        
        print("Indique fecha inicial:")
        initial_date = self.__get_y_m_d()
        initial_date_str = initial_date.strftime('%d/%m/%Y')
        
        print("Indique fecha final:")
        final_date = self.__get_y_m_d()
        final_date_str = final_date.strftime('%d/%m/%Y')
        
        orders_counter = 0
        accum_profit = 0
        detail_ = ""
        for order in self.orders:
            delivered_date = order.getDelivered_date()
            delivered_date = delivered_date.date()
            if initial_date <= delivered_date <= final_date:
                orders_counter += 1
                final_profit = order.getFinal_price()
                accum_profit += final_profit
                detail_ += (str(order) + "\n")
        print(f"Ganancia acumulada entre el {initial_date_str} y el"
              f"{final_date_str}: $ {accum_profit}")
        print("Desea ver el detalle? (S/N)")
        answ_ = return_S_N()
        if answ_ == "S":
            print(f"Se tuvieron {orders_counter} pedidos en el periodo "
                  "especificado. A continuacion se da detalle de los mismos:")
            print(detail_)
        
    def most_popular(self):
        most_popular_variety = "Atencion! No se cargaron pedidos aun!"
        most_popular_type = {"name":"Atencion! No se cargaron pedidos aun!"}
        print("La variedad mas solicitada es:")
        varieties_aux_list = list()
        for order in self.orders:
            for variety in order.getOrder_varieties():
                varieties_aux_list.append(variety)
        
        varieties_aux_list_names = list()
        for v in varieties_aux_list:
            varieties_aux_list_names.append(v.getNombre())
        max_ = 0
        for v_nombre in varieties_aux_list_names:
            x = varieties_aux_list_names.count(v_nombre)
            if x > max_:
                max_ = x
                most_popular_variety = v_nombre
        print(f"{most_popular_variety} con {max_} pedidos totales")#type: ignore
               
        print("El tipo mas pedido es: ")
        varieties_type_aux_list = list()
        for v in varieties_aux_list:
            varieties_type_aux_list.append(v.getTipo())
        max_ = 0
        for v_type in varieties_type_aux_list:
            x = varieties_type_aux_list.count(v_type)
            if x > max_:
                max_ = x
                most_popular_type = v_type
        print(f"{most_popular_type['name']} con {max_} pedidos totales")#type: ignore
    
class Order:
    def __init__(self, menu_varieties:list):
        self.order_varieties = list() #type:list[Variety]
        self.final_price = float()
        # self.fecha_entrega = datetime.datetime(0, 0, 0) 
        self.delivered_date_str = ""
        self.client = self.__ask_client()
        print("Seleccione de entre las variedades de pizza indicando su "
              "codigo y cantidad:")
        self.__show_variedades(menu_varieties)
        
        total_delay = self.final_price = 0
        unit_delay = 10 #minutos
        id_quantity_list = self.__ask_variedad(menu_varieties)
        for id_, quantity in id_quantity_list:
            index_ = id_ - 1          
            variety = menu_varieties[index_] #type: Variety
            for i in range(quantity):
                self.order_varieties.append(variety)
                self.final_price += variety.getPrice()
                total_delay += unit_delay
        # se añaden la variedades pedidas a la lista de variedades del pedido
        print("\nSe anotaron las variedades con sus cantidades. Demora "
              f"estimada: {total_delay} minutos. Precio final: $ "
              f"{self.final_price}. Detalle: ")
        for v in self.order_varieties:
            print(v)
        print("")
        self.delivered_date = (datetime.datetime.now() + 
                              datetime.timedelta(minutes=total_delay))
        self.delivered_date_str = (
            self.delivered_date.strftime('%d/%m/%Y %H:%M:%S'))
        print(f"Fecha y hora de entrega estimada: {self.delivered_date_str}")
   
        # CON LAS IDS vamos a obtener las variedades originales!
        # y luego con las cantidades podemos determinar el precio final

    def __str__(self) -> str:
        string_ = (f"Fecha entregado: {self.delivered_date_str} - Cliente: "
                f"{self.client}. - Precio final: $ {self.final_price} - "
                f"Detalle:\n")
        for variety in self.order_varieties:
            string_ += str(variety) + "\n"
        return string_
        
    def __show_variedades(self,  varieties_menu:list):
        for variety_menu in varieties_menu:
            print(variety_menu)
            print("-"*50)
    
    def __ask_variedad(self, varieties_menu:list):
        '''returns the code of the variety and the quantity of it'''
        varieties_list = list()
        while(True):
            print("Indique el codigo de la variedad: (0 para salir)")
            id_ = check_range(convert_to_int(input("\t")), 0,
                                 len(varieties_menu))
            if id_ == 0:
                print("Finalizando carga de variedades")
                break
            else:
                print("Indicar la cantidad de pizzas (ENTER para 1)")
                quantity = input("\t")
                if quantity.strip() == "":
                    quantity = 1
                quantity = check_non_negative_int(convert_to_int(quantity))
                varieties_list.append((id_, quantity))
        return varieties_list
                        
    def __ask_client(self):
        print("Introducir el nombre del cliente: ")
        while(True):
            name = input("\t").strip().upper()
            print(f"El nombre \"{name}\" es correcto? (S/N)")
            x = input("\t").strip().upper()
            while(True):
                if x not in ("S","N"):
                    print("Valor invalido. Reintentar:")
                    x = input("\t").strip().upper()
                else:
                    break
            if x == "S":
                print("Nombre registrado.")
                return name
            else: # x == "N":
                print("Por favor, introducir otro nombre:")
    
    def getOrder_varieties(self):
        return self.order_varieties
    def setOrder_varieties(self, order_varieties):
        self.order_varieties = order_varieties
    def getFinal_price(self):
        return self.final_price
    def setFinal_price(self, final_price):
        self.final_price = final_price
    def getDelivered_date(self):
        return self.delivered_date
    def setDelivered_date(self, delivered_date):
        self.delivered_date = delivered_date
    def getDelivered_date_str(self):
        return self.delivered_date_str
    def setDelivered_date_str(self, delivered_date_str):
        self.delivered_date_str = delivered_date_str
    def getClient(self):
        return self.client
    def setClient(self, client):
        self.client = client
                
class Variety: # para generacion automatica
    sizes = [{"name":"normal","size":8,"added_price":15},
                {"name":"grande","size":10,"added_price":18},
                {"name":"extra grande","size":12,"added_price":20}]
    types = [{"name":"a la piedra","added_price":10},
            {"name":"a la parrilla","added_price":8},
            {"name":"de molde","added_price":12}]
   # def __init__(self, nombre_base, tamanio_n:int, tipo_n:int):
    def __init__(self, id_:int, base_name:str, base_price:int, size_num:int, 
                 type_num:int, ingredients:list[str]):
        self.id_ = id_
        # tamanio = {"name":"x","size":x,"added_price":x}
        self.size = self.sizes[size_num] 
        # tipo = {"name":"x","added_price":x}
        self.type = self.types[type_num]
        self.name = (base_name + " " + self.size["name"] + " " +
                       self.type["name"]) # str
        self.ingredients = ingredients
        self.price = (base_price + self.size["added_price"] + 
                       self.type["added_price"]) #int.
    def __str__(self) -> str:
        ingredients_list_str = ", ".join(self.ingredients)
        return (f"Codigo ({self.id_}) - {self.name} - Porciones: " +
                   f"{self.size['size']}\n\tIngredientes: "
                   f"{ingredients_list_str}\t\tPrecio: $ {self.price}")
    
    def getId_(self):
        return self.id_
    def setId_(self, id_):
        self.id_ = id_
    def getSize(self):
        return self.size
    def setSize(self, size):
        self.size = size
    def getType(self):
        return self.type
    def setType(self, type):
        self.type = type
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getIngredients(self):
        return self.ingredients
    def setIngredients(self, ingredients):
        self.ingredients = ingredients
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price   