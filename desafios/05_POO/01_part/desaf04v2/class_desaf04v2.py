# contacto: diccionario. ej:
#               {name: "marcelo", num: "3644 414344", email: "abc@x.com"}
# Agenda: lista de contactos
# ej: [ {name: "marcelo", num: "3644 414344", email: "abc@x.com"}, ... ]

class Contact:
    def __init__(self, name, num, email):
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


class Agenda:    
    def __init__(self):
        self.contacts = list() # vamos a usar una lista de diccionarios

    def __getsInfo(self): 
        name = input("Nombre:\n\t").title()
        num =  input("Telefono:\n\t")
        email = input("Email: \n\t")
        return name, num, email

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
                             f"(S/N)\n\t").upper()
            if this_one not in ("S","N"):
                print("Valor erroneo, reintentar.")
                continue
            else:
                if this_one == 'N':
                    return False
                else:
                    return True

    def add_contact(self): 
        print("Ingrese los datos del contacto nuevo: ")
        name, num, email = self.__getsInfo()
        contact = Contact (name, num, email)
        self.contacts.append(contact)
    
    def show_contact_list(self): 
        for contact in self.contacts:
            print (f"Nombre: {contact.getName()}, Telefono: {contact.getNum()}"
                   f", Email: {contact.getEmail()}")
       
    def __sorts_agenda(self): 
        '''sorts an Agenda by the name of the object Contact'''
        def returns_name_value(contact_):
            return (contact_.getName())
        
        self.contacts.sort(key = returns_name_value)
        # https://docs.python.org/3/howto/sorting.html#:~:text=sort()%20and%20sorted(),element%20prior%20to%20making%20comparisons.&text=The%20value%20of%20the%20key,to%20use%20for%20sorting%20purposes. 
    
    def search_contact(self): 
        search_by = self.__search_by_()
        counter_ = 0
        string_aux = ""
        if search_by == "1":
            name_x = input("Indique el nombre del contacto:\n\t").title()
            for contact in self.contacts:
                if contact.getName() == name_x:
                    counter_ += 1
                    string_aux = (string_aux + f"Nombre: {contact.getName()}, "
                                  f"Telefono: {contact.getNum()}, "
                                  f"Email: {contact.getEmail()}\n")
            print(f"Encontradas {counter_} coincidencias con el nombre "
                  f"{name_x}:\n{string_aux}")
        elif search_by == "2":
            number_x = input("Indique el numero del contacto:\n\t")
            for contact in self.contacts:
                if contact.getNum() == number_x:
                    counter_ += 1
                    string_aux = (string_aux + f"Nombre: {contact.getName()}, "
                                  f"Telefono: {contact.getNum()}, "
                                  f"Email: {contact.getEmail()}\n")
            print(f"Encontradas {counter_} coincidencias con el numero de "
                  f"telefono {number_x}:\n{string_aux}")               
    
    def edit_contact(self): 
        print("Que contacto desea modificar?")
        search_by = self.__search_by_()
        if search_by == "1":
            name_x = input("Indique el nombre del contacto:\n\t").title()
            
            for contact in self.contacts:
                
                if contact.getName() == name_x:
                    print(f"Nombre: {contact.getName()}, Telefono: "
                          f"{contact.getNum()}, Email: {contact.getEmail()}")
                    this_one = self.__this_one("editar") 
                    if this_one:
                        print("Ingrese nuevos datos: ")
                        new_name, new_num, new_email = self.__getsInfo() 
                        contact.setName(new_name)
                        contact.setNum(new_num)
                        contact.setEmail(new_email)
                        print("Contacto modificado!")
                        return None
                    else:
                        print("Mostrando siguiente coincidencia:")
                        continue
            print(f"No se encontraron coincidencias para el nombre {name_x}")
        elif search_by == "2":
            number_x = input("Indique el numero del contacto:\n\t")
            for contact in self.contacts:
                if contact.getNum() == number_x:
                    print(f"Nombre: {contact.getName()}, Telefono: "
                        f"{contact.getNum()}, Email: {contact.getEmail()}")
                    this_one = self.__this_one("editar")
                    if this_one:
                        print("Ingrese nuevos datos: ")
                        new_name, new_num, new_email = self.__getsInfo()
                        contact.setName(new_name)
                        contact.setNum(new_num)
                        contact.setEmail(new_email)
                        print("Contacto modificado!")
                        return None
                    else:
                        print("Mostrando siguiente coincidencia:")
                        continue
            print(f"No se encontraron coincidencias para el numero {number_x}")
   
    def delete_contact(self): 
        print("Que contacto desea borrar?")
        search_by = self.__search_by_()
        if search_by == "1":
            name_x = input("Indique el nombre del contacto:\n\t").title()
            aux_i = -1
            for contact in self.contacts:
                aux_i += 1
                if contact.getName() == name_x:
                    print(f"Nombre: {contact.getName()}, Telefono: "
                          f"{contact.getNum()}, Email: {contact.getEmail()}")
                    this_one = self.__this_one("borrar")
                    if this_one:
                        self.contacts.remove(contact)
                        print("Contacto eliminado!")
                        return None
                    else:
                        print("Mostrando siguiente coincidencia:")
                        continue
            print(f"No se encontraron coincidencias para el nombre {name_x}")
        elif search_by == "2":
            number_x = input("Indique el numero del contacto:\n\t")
            for contact in self.contacts:
                if contact.getNum() == number_x:
                    print(f"Nombre: {contact.getName()}, Telefono: "
                        f"{contact.getNum()}, Email: {contact.getEmail()}")
                    this_one = self.__this_one("borrar")
                    if this_one:
                        self.contacts.remove(contact)
                        print("Contacto eliminado!")
                        return None
                    else:
                        print("Mostrando siguiente coincidencia:")
                        continue
            print(f"No se encontraron coincidencias para el numero {number_x}")
   
    def __aux_menu(self): 
        while(True):
            print("INDICAR OPERACION:\n\tAñadir contacto\t\t(1)\n\tLista de "
                  "contactos\t(2)\n\tBuscar contacto\t\t(3)\n\tEditar contacto"
                  "\t\t(4)\n\tEliminar contacto\t(5)\n\n\tCerrar Agenda\t\t(0)")
            x = input("\t").strip()
            if x not in ("0", "1", "2", "3", "4", "5"):
                print("Error. Reintentar ingreso de operacion.")
                continue
            return x
            
    def menu(self):
        while(True):
            op = self.__aux_menu()
            self.__sorts_agenda()
            if op == "0":
                print("Saliendo de agenda")
                return None
            elif op == "1":
                self.add_contact()
            elif op == "2":
                self.show_contact_list()
            elif op == "3":
                self.search_contact()
            elif op == "4":
                self.edit_contact()
            else:
                self.delete_contact()
