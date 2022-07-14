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