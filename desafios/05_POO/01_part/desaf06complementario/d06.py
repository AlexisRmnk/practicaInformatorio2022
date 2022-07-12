# GESTIÓN DE DONACIONES
# https://sites.google.com/view/informatorio-poo/level-stone/level-stone#h.pbeev0bxu6be

class Product:
    def __init__(self, name:str, amount:int):
        self.name = name
        self.amount = amount

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getAmount(self):
        return self.amount
    def setAmount(self, amount):
        self.amount = amount

    def calculate(self, entities:int):
        amount_to_send = self.amount//entities
        remaining = self.amount%entities
        return amount_to_send, remaining

class Perishable(Product):
    def __init__(self, name: str, amount: int, days_to_expire:int):
        super().__init__(name, amount)
        self.days_to_expire = days_to_expire 
    
    def getDays_to_expire(self):
        return self.days_to_expire
    def setDays_to_expire(self, days_to_expire):
        self.days_to_expire = days_to_expire
    
    def calculate(self, entities: int):
        amount_to_send, remaining = super().calculate(entities)
        print(f"Se debera enviar {amount_to_send} productos a cada una de las"
              f" {entities} entidades. Quedara un sobrante de {remaining} "
              f"productos")
        if self.days_to_expire < 10:
            print(f"Quedan {self.days_to_expire} dias para que expire el"
                  " producto. La entrega debe hacerse en el dia actual.")
        elif self.days_to_expire < 31: 
            print(f"Quedan {self.days_to_expire} dias para que expire el prod"
                  "ucto. La entrega debe hacerse en el plazo de una semana")
        self.setAmount(remaining) 
        
class NonPerishable(Product):
    def __init__(self, name: str, amount: int, type_ : str):
        super().__init__(name, amount)
        self.type_ = type_
    
    def getType_(self):
        return self.type_
    def setType_(self, type_):
        self.type_ = type_
        
    def calculate(self, entities: int):
        amount_to_send, remaining = super().calculate(entities)
        print(f"Se debera enviar {amount_to_send} productos a cada una de las"
              f" {entities} entidades. Quedara un sobrante de {remaining} "
              f"productos")
        print("La entrega debe hacerse antes del mes.")
        self.setAmount(remaining) 

def return_1or2():
    while(True):
        print("El producto es perecedero? ('1' --- SI, '2' --- NO)")
        x = input("\t").strip()
        if x not in ("1","2"):
            print("Valor incorrecto, reintentar.")
            continue
        return x
            
    
def return_int(string_:str):
    while(True):
        try:
            int_ = int(string_)
            return int_
        except:
            print("Valor invalido, debe ser numerico entero. Reintentar: ")
            string_ = input("\t")
            continue
    
while(True):
    print("Indicar nombre del producto.")
    name = input("\t")
    print("Indicar cantidad del producto.")
    amount = return_int(input("\t"))
    print("Indicar cantidad de entidades a considerar.")
    ent = return_int(input("\t"))
    x = return_1or2()
    if x == "1":
        print("Indicar dias para que el producto expire:")
        days = return_int(input("\t"))
        p = Perishable(name, amount, days)
        p.calculate(ent)
    elif x == "2":
        print("Indicar tipo del producto no perecedero:")
        type_ = input("\t")
        np = NonPerishable(name, amount, type_)
        np.calculate(ent)
        
    print("Desea volver a calcular? ('ENTER' para continuar, '0' para salir)")
    x = input("\t")
    if x == "0":
        print("Finalizando ejecucion.")
        break

