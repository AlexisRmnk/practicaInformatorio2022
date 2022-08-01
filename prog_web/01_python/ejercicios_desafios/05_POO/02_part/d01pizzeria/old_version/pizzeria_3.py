import datetime
import random

class Pizzeria:
    def __init__(self) -> None:
        self.pedidos = list() #type: list[Pedido]
        
        #tipo : list[Variedad]
        self.variedades_menu = self.__generar_variedades_menu()
        
    
    def __generar_variedades_menu(self):
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
        variedades_menu = list()
        codigo = 1
        for var_x in vars:
            for tamanio_n in range(3):
                for tipo_n in range(3):
                    new_var = Variedad(codigo, var_x["name"], var_x["price"], 
                                       tamanio_n, tipo_n, var_x["ingredients"])
                    codigo = codigo + 1
                    variedades_menu.append(new_var)
        return variedades_menu
                    
    def modificar_fechas_pedidos(self):
        '''Modifies dates on orders by subtracting 1 to 30 days randomly'''
        print("Esta seguro que desea modificar las fechas? (S/N)"
              "ACCION NO REVERSIBLE")
        answ_ = return_S_N()
        if answ_ == "S":
            for pedido in self.pedidos:
                date_1 = pedido.getFecha_entrega()
                date_1_mod = date_1 - datetime.timedelta(
                    days= random.randint(1, 30)) 
                date_1_mod_str = date_1_mod.strftime('%d/%m/%Y %H:%M:%S')
                pedido.setFecha_entrega(date_1_mod)
                pedido.setFecha_entrega_str(date_1_mod_str)
        else:
            print("Accion abortada.")
            
                
    def generar_pedido(self):
        pedido = Pedido(self.variedades_menu)
        self.pedidos.append(pedido)

    def ver_pedidos(self):
        i=0
        for pedido in self.pedidos:
            i+=1
            print("-"*50)
            print(f"--- Pedido N°{i} " + "-"*30)
            print(pedido)
            print("-"*50)

    def __get_y_m_d(self):
        '''Asks and returns a date'''
        print("Año:")
        anio = check_range(check_non_negative_int(
            convert_to_int(input("\t"))), 1900, 2100)
        print("Mes:")
        mes = check_range(check_non_negative_int(
            convert_to_int(input("\t"))), 1, 12)
        dia_max = month_days(mes, anio)
        print("Dia:")
        dia = check_range(check_non_negative_int(
            convert_to_int(input("\t"))), 1, dia_max) #type: ignore
        return datetime.date(anio, mes, dia)
        

    def recaudaciones_tiempo(self): 
        '''Prints income and detail for a given period'''
        
        print("Indique fecha inicial:")
        fecha_inicial = self.__get_y_m_d()
        fecha_inicial_str = fecha_inicial.strftime('%d/%m/%Y')
        
        print("Indique fecha final:")
        fecha_final = self.__get_y_m_d()
        fecha_final_str = fecha_final.strftime('%d/%m/%Y')
        
        contador_pedidos = 0
        ganancia_acumulada = 0
        detail_ = ""
        for pedido in self.pedidos:
            fecha_entrega = pedido.getFecha_entrega()
            fecha_entrega = fecha_entrega.date()
            if fecha_inicial <= fecha_entrega <= fecha_final:
                contador_pedidos += 1
                ganancia_final = pedido.getPrecio_final()
                ganancia_acumulada += ganancia_final
                detail_ += (str(pedido) + "\n")
        print(f"Ganancia acumulada entre el {fecha_inicial_str} y el"
              f"{fecha_final_str}: $ {ganancia_acumulada}")
        print("Desea ver el detalle? (S/N)")
        answer_ = return_S_N()
        if answer_ == "S":
            print(f"Se tuvieron {contador_pedidos} pedidos en el periodo "
                  "especificado. A continuacion se da detalle de los mismos:")
            print(detail_)
        

    def mas_solicitadas(self):
        variedad_mas_pedida = "Atencion! No se cargaron pedidos aun!"
        tipo_mas_pedido = {"name":"Atencion! No se cargaron pedidos aun!"}
        print("La variedad mas solicitada es:")
        variedades_lista_aux = list()
        for pedido in self.pedidos:
            for variedad in pedido.getVariedades_pedido():
                variedades_lista_aux.append(variedad)
        
        variedades_nombres_lista_aux = list()
        for v in variedades_lista_aux:
            variedades_nombres_lista_aux.append(v.getNombre())
        max_ = 0
        for v_nombre in variedades_nombres_lista_aux:
            x = variedades_nombres_lista_aux.count(v_nombre)
            if x > max_:
                max_ = x
                variedad_mas_pedida = v_nombre
        print(f"{variedad_mas_pedida} con {max_} pedidos totales")#type: ignore
               
        print("El tipo mas pedido es: ")
        variedades_tipos_lista_aux = list()
        for v in variedades_lista_aux:
            variedades_tipos_lista_aux.append(v.getTipo())
        max_ = 0
        for v_tipo in variedades_tipos_lista_aux:
            x = variedades_tipos_lista_aux.count(v_tipo)
            if x > max_:
                max_ = x
                tipo_mas_pedido = v_tipo
        print(f"{tipo_mas_pedido['name']} con {max_} pedidos totales")#type: ignore
    
    
    
class Pedido:
    def __init__(self, variedades_menu:list):
        self.variedades_pedido = list() #type:list[Variedad]
        self.precio_final = float()
        # self.fecha_entrega = datetime.datetime(0, 0, 0) 
        self.fecha_entrega_str = ""
        self.cliente = self.__ask_client()
        print("Seleccione de entre las variedades de pizza indicando su "
              "codigo y cantidad:")
        self.__show_variedades(variedades_menu)
        
        demora_total = self.precio_final = 0
        demora_unitaria = 10 #minutos
        lista_id_cant = self.__ask_variedad(variedades_menu)
        for codigo, cantidad in lista_id_cant:
            indice = codigo - 1          
            variedad = variedades_menu[indice] #type: Variedad
            for i in range(cantidad):
                self.variedades_pedido.append(variedad)
                self.precio_final += variedad.getPrecio()
                demora_total += demora_unitaria
        # se añaden la variedades pedidas a la lista de variedades del pedido
        print("\nSe anotaron las variedades con sus cantidades. Demora "
              f"estimada: {demora_total} minutos. Precio final: $ "
              f"{self.precio_final}. Detalle: ")
        for v in self.variedades_pedido:
            print(v)
        print("")
        fecha_actual = datetime.datetime.now()
        self.fecha_entrega = (fecha_actual + 
                              datetime.timedelta(minutes=demora_total))
        self.fecha_entrega_str = (
            self.fecha_entrega.strftime('%d/%m/%Y %H:%M:%S'))
        print(f"Fecha y hora de entrega estimada: {self.fecha_entrega_str}")
   
        # CON LAS IDS vamos a obtener las variedades originales!
        # y luego con las cantidades podemos determinar el precio final

    def __str__(self) -> str:
        string_ = (f"Fecha entregado: {self.fecha_entrega_str} - Cliente: "
                f"{self.cliente}. - Precio final: $ {self.precio_final} - "
                f"Detalle:\n")
        for variedad in self.variedades_pedido:
            string_ += str(variedad) + "\n"
        return string_
        
       

        
    def __show_variedades(self,  variedades_menu:list):
        for variedad_menu in variedades_menu:
            print(variedad_menu)
            print("-"*50)
    
    def __ask_variedad(self, variedades_menu:list):
        '''returns the code of the variety and the quantity of it'''
        variedades_lista = list()
        while(True):
            print("Indique el codigo de la variedad: (0 para salir)")
            codigo = check_range(convert_to_int(input("\t")), 0,
                                 len(variedades_menu))
            if codigo == 0:
                print("Finalizando carga de variedades")
                break
            else:
                print("Indicar la cantidad de pizzas (ENTER para 1)")
                cant = input("\t")
                if cant.strip() == "":
                    cant = 1
                cant = check_non_negative_int(convert_to_int(cant))
                variedades_lista.append((codigo, cant))
        return variedades_lista
                
                
                
    def __ask_client(self):
        print("Introducir el nombre del cliente: ")
        while(True):
            nombre = input("\t").strip().upper()
            print(f"El nombre \"{nombre}\" es correcto? (S/N)")
            x = input("\t").strip().upper()
            while(True):
                if x not in ("S","N"):
                    print("Valor invalido. Reintentar:")
                    x = input("\t").strip().upper()
                else:
                    break
            if x == "S":
                print("Nombre registrado.")
                return nombre
            else: # x == "N":
                print("Por favor, introducir otro nombre:")
    
    def getVariedades_pedido(self):
        return self.variedades_pedido
    def setVariedades_pedido(self, variedades_pedido):
        self.variedades_pedido = variedades_pedido
    def getPrecio_final(self):
        return self.precio_final
    def setPrecio_final(self, precio_final):
        self.precio_final = precio_final
    def getFecha_entrega(self):
        return self.fecha_entrega
    def setFecha_entrega(self, fecha_entrega):
        self.fecha_entrega = fecha_entrega
    def getFecha_entrega_str(self):
        return self.fecha_entrega_str
    def setFecha_entrega_str(self, fecha_entrega_str):
        self.fecha_entrega_str = fecha_entrega_str
    def getCliente(self):
        return self.cliente
    def setCliente(self, cliente):
        self.cliente = cliente
                
class Variedad: # para generacion automatica
    tamanios = [{"name":"normal","size":8,"added_price":15},
                {"name":"grande","size":10,"added_price":18},
                {"name":"extra grande","size":12,"added_price":20}]
    tipos = [{"name":"a la piedra","added_price":10},
            {"name":"a la parrilla","added_price":8},
            {"name":"de molde","added_price":12}]
   # def __init__(self, nombre_base, tamanio_n:int, tipo_n:int):
    def __init__(self, codigo:int, nombre_base:str, precio_base:int, tamanio_n:int, 
                 tipo_n:int, ingredientes:list[str]):
        self.codigo = codigo
        # tamanio = {"name":"x","size":x,"added_price":x}
        self.tamanio = self.tamanios[tamanio_n] 
        # tipo = {"name":"x","added_price":x}
        self.tipo = self.tipos[tipo_n]
        self.nombre = (nombre_base + " " + self.tamanio["name"] + " " +
                       self.tipo["name"]) # str
        self.ingredientes = ingredientes
        self.precio = (precio_base + self.tamanio["added_price"] + 
                       self.tipo["added_price"]) #int.
    def __str__(self) -> str:
        lista_ingredientes_str = ", ".join(self.ingredientes)
        return (f"Codigo ({self.codigo}) - {self.nombre} - Porciones: " +
                   f"{self.tamanio['size']}\n\tIngredientes: "
                   f"{lista_ingredientes_str}\t\tPrecio: $ {self.precio}")
    
    def getCodigo(self):
        return self.codigo
    def setCodigo(self, codigo):
        self.codigo = codigo
    def getTamanio(self):
        return self.tamanio
    def setTamanio(self, tamanio):
        self.tamanio = tamanio
    def getTipo(self):
        return self.tipo
    def setTipo(self, tipo):
        self.tipo = tipo
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    def getIngredientes(self):
        return self.ingredientes
    def setIngredientes(self, ingredientes):
        self.ingredientes = ingredientes
    def getPrecio(self):
        return self.precio
    def setPrecio(self, precio):
        self.precio = precio   
        
        
def check_non_negative_int(x):
    while(True):
        try:
            x = int(x)
            if x < 0:
                print(f"{x} es un valor negativo. Ingresar un valor entero"
                        " mayor o igual a 0:")    
                x = input("\t")  
                continue
            else:
                return x        
        except:
            print(f"{x} no es un valor numerico entero. Volver a ingresar:")
            x = input("\t")

def convert_to_int(x):
    '''
    Use with an input. It checks out if the input is an integer!
    '''
    while(True):
        try:
            return int(x)
        except:
            print(f"El valor {x} no es un numero entero. Reintentar.")
            x = input("\t")
            continue
        
def check_range(x:int, bottom_n:int, top_n:int):
    ''' 
    continues if x is an integer between "bottom_n" and "top_n"
    ex:     check_range(17, 1, 10) makes you change 17 for another number. 
            check_range(5, 1, 10) returns 5. 
    '''
    while(True):
        try:
            if(bottom_n <= x <= top_n):
                return x
            else:
                print(f"{x} no es un valor entero comprendido entre "
                    f"{bottom_n} y {top_n}. Reintentar operacion.")
                x = convert_to_int(input("\t"))
        except:
            x = convert_to_int(input("\t"))

def month_days(month: int, year: int):
    '''
    Returns the amount of days in a month given its year.
    '''
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        if leap_year(year):
            return 29
        else:
            return 28
    else: 
        print("Mes incorrecto (Mes debe valer entre 1 y 12)")
        pass

def leap_year(year: int) -> bool:
    ''' 
    Returns True if the year is a leap year
    ex: 2004 returns True, 2003 returns False
    '''
    if year%4 == 0:
        return True
    else: 
        return False

def return_S_N():
    print("Validar (S - si / N - no)")
    while(True):
        x = input("\t").strip().upper()
        if x in ("S","N"):
            return x
        else:
            print("Carater invalido. Reintentar\n")

# MAIN TESTING

def main():
    p = Pizzeria()
    while(True):
        op = returns_option()
        if op == "0":
            print("Finalizando ejecucion.")
            break
        elif op == "1":
            p.generar_pedido()
            print("Pedido generado")
        elif op == "2":
            p.ver_pedidos()
        elif op == "3":
            p.mas_solicitadas()
        elif op == "4": # TESTEAR
            p.recaudaciones_tiempo()
        elif op == "5":
            p.modificar_fechas_pedidos()
    
    
        
def returns_option():
    print("PIZZERIA MENU")
    while(True):
            print("INDICAR OPERACION:\n\t0) Finalizar programa\n\t"
                  "1) Añadir pedido\n\t2) Mostrar pedidos\n\t3) "
                  "Mostrar variedades y tipos mas solicitados\n\t4) "
                  "Mostrar recaudaciones y detalle de pedidos dado un "
                  "periodo de tiempo.\n\t5) Modificar fechas pedidos "
                  "para realizar pruebas")
            x = input("\t").strip()
            if x not in ("0", "1", "2", "3", "4", "5"):
                print("Error. Reintentar ingreso de operacion.")
                continue
            return x        
        

main()