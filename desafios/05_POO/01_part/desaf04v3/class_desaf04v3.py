# contacto: diccionario. ej:
#               {name: "marcelo", num: "3644 414344", email: "abc@x.com"}
# Agenda: lista de contactos
# ej: [ {name: "marcelo", num: "3644 414344", email: "abc@x.com"}, ... ]

class Contact:
    def __init__(self):
        print("Ingrese los datos del contacto nuevo: ")
        name, num, email = self.asks_info()
        self.name = name
        self.num = num
        self.email = email
    
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getNum(self):
        return self.num
    def setNum(self, num):
        self.num = num
    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email = email 
        
    def edit_contact(self):
        print("Ingrese nuevos datos: ")
        new_name, new_num, new_email = self.asks_info()
        self.name = new_name
        self.num = new_num
        self.email = new_email
        print("Contacto modificado!")
        
    def return_contact(self):
        return (f"Nombre: {self.name}, Telefono: {self.num}, Email: "
                f"{self.email}")

    def asks_info(self): 
        name = input("Nombre:\n\t").title()
        num =  input("Telefono:\n\t")
        email = input("Email: \n\t")
        return name, num, email

class Agenda:    
    def __init__(self):
        self.contacts = list() # vamos a usar una lista de objetos "Contacto"


    def __search_by_(self):
        '''Returns 1 if the search is by NAME, and 2 if it is by TEL'''
        while(True):
            print("Indique si desea buscar contacto por Nombre (1) o Numero de"
                " telefono (2)")
            search_by = input("\t").strip()
            if search_by not in ("1","2"):
                print("Seleccion incorrecta. Reintentar operacion.")
                continue
            else:
                break
        return search_by
    
    def __this_one(self, op:str): 
        while(True):
            this_one = input(f"Este es el contacto que desea {op}? "
                             f"(S/N)\n\t").upper().strip()
            if this_one not in ("S","N"):
                print("Valor erroneo, reintentar.")
                continue
            else:
                return this_one == 'S' # True when 'S'. False when 'N'

    def add_contacts(self): 
        contact = Contact()
        self.contacts.append(contact)
    
    def show_contact_list(self): 
        for contact in self.contacts:
            print (f"Nombre: {contact.getName()}, Telefono: {contact.getNum()}"
                   f", Email: {contact.getEmail()}")
       
    def sorts_agenda(self): 
        ''' 
        Sorts an agenda by the first key value ("name" in this case).
        An agenda is a list of objects "Contact"
        '''
        def returns_name_value(contact_):
            return (contact_.getName())
        
        self.contacts.sort(key = returns_name_value)
        # https://docs.python.org/3/howto/sorting.html#:~:text=sort()%20and%20sorted(),element%20prior%20to%20making%20comparisons.&text=The%20value%20of%20the%20key,to%20use%20for%20sorting%20purposes. 
    
    
    def search_contacts(self): 
        search_by = self.__search_by_()
        counter_ = 0
        string_aux = ""
        if search_by == "1":
            name_x = input("Indique el nombre del contacto:\n\t").title()
            for contact in self.contacts:
                if contact.getName() == name_x:
                    counter_ += 1
                    string_aux = string_aux + contact.return_contact() + "\n"
            print(f"Encontradas {counter_} coincidencias con el nombre "
                  f"{name_x}:\n{string_aux}")
        elif search_by == "2":
            number_x = input("Indique el numero del contacto:\n\t")
            for contact in self.contacts:
                if contact.getNum() == number_x:
                    counter_ += 1
                    string_aux = string_aux + contact.return_contact() + "\n"
            print(f"Encontradas {counter_} coincidencias con el numero de "
                  f"telefono {number_x}:\n{string_aux}")               
    
    def edit_contacts(self): 
        print("Que contacto desea modificar?")
        search_by = self.__search_by_()
        if search_by == "1":
            name_x = input("Indique el nombre del contacto:\n\t").title()
            
            for contact in self.contacts:
                if contact.getName() == name_x:
                    print(contact.return_contact())
                    this_one = self.__this_one("editar") 
                    if this_one:
                        contact.edit_contact()
                        return
                    else:
                        print("Mostrando siguiente coincidencia:")
                        continue
            print(f"No se encontraron coincidencias para el nombre {name_x}")
        elif search_by == "2":
            number_x = input("Indique el numero del contacto:\n\t")
            for contact in self.contacts:
                if contact.getNum() == number_x:
                    print(contact.return_contact())
                    this_one = self.__this_one("editar")
                    if this_one:
                        contact.edit_contact()
                        return
                    else:
                        print("Mostrando siguiente coincidencia:")
                        continue
            print(f"No se encontraron coincidencias para el numero {number_x}")
   
    def delete_contacts(self): 
        print("Que contacto desea borrar?")
        search_by = self.__search_by_()
        if search_by == "1":
            name_x = input("Indique el nombre del contacto:\n\t").title()
            for contact in self.contacts:
                if contact.getName() == name_x:
                    print(contact.return_contact())
                    this_one = self.__this_one("borrar")
                    if this_one:
                        self.contacts.remove(contact)
                        print("Contacto eliminado!")
                        return
                    else:
                        print("Mostrando siguiente coincidencia:")
                        continue
            print(f"No se encontraron coincidencias para el nombre {name_x}")
        elif search_by == "2":
            number_x = input("Indique el numero del contacto:\n\t")
            for contact in self.contacts:
                if contact.getNum() == number_x:
                    print(contact.return_contact())
                    this_one = self.__this_one("borrar")
                    if this_one:
                        self.contacts.remove(contact)
                        print("Contacto eliminado!")
                        return
                    else:
                        print("Mostrando siguiente coincidencia:")
                        continue
            print(f"No se encontraron coincidencias para el numero {number_x}")