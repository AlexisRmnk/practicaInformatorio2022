# autogetter y setter
# author: Alexis Romaniuk

def getter_ (string_:str):
    atribute_ = string_[5:]
    return f'''def get_{atribute_}(self):
        return self.{atribute_}'''
    
def setter_ (string_:str):
    atribute_ = string_[5:]
    return f'''def set_{atribute_}(self, {atribute_}):
        self.{atribute_} = {atribute_}'''

def validation_ (string_:str):
    if "self." == string_[0:5] and string_[5:].isalnum():
        return True
    else:
        return False

while(True):
    string_ = input("\nIngresar cadena con atributo ('0' para salir)."
                    "\nEJ: self.attribute1\n\t")
    string_.strip()
    if string_ == "0":
        print("Saliendo de programa")
        break
    if not validation_(string_):
        print("Valor invalido, recordar poner atributo con la forma "
              "'self.attribute1'")
        continue
    print(f"METODO GET:\n{getter_(string_)}")
    print(f"METODO SET:\n{setter_(string_)}")
    
    
    
    
    
    
    
