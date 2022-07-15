# autogetter y setter
# author: Alexis Romaniuk

def getter_ (atribute_:str):
    return f'''def get_{atribute_}(self):
    return self.{atribute_}'''
    
def setter_ (atribute_:str):
    return f'''def set_{atribute_}(self, {atribute_}):
    self.{atribute_} = {atribute_}'''

def validation_ (string_:str):
    #if "self." == string_[0:5] and string_[5:].isalnum():
    # Formato de Ejemplo: self.atributo1
    if string_.isalnum():
        return True
    else:
        return False

def list_atts():
    print(("\nIngresar cadenas con atributos ('ENTER' para ingresar"
           " siguiente atributo, '0' para finalizar carga de atributos)."
            "\nFormato de Ejemplo: 'atributo1'\n\t"))
    list_of_atts = list()
    i = 1
    while(True):
        print(f"ATRIBUTO {i}:")
        string_ = input("\t")
        string_.strip()
        if string_ == "0":
            print("Finalizando carga de atributos\n")
            break   
        if not validation_(string_):
            print("Valor invalido, recordar poner atributo con la forma "
                "'atributo1'")
            continue
        else:
            i+=1
            list_of_atts.append(string_)
    return list_of_atts

def auto_get_set(list_of_atts_:list):
    for att in list_of_atts_:
        print(getter_(att))
    print("")
    for att in list_of_atts_:
        print(setter_(att))    
        
def auto_get_set2(list_of_atts_:list):
    for att in list_of_atts_:
        print(getter_(att))
        print(setter_(att))        
         
# MAIN
list_of_atts = list_atts()
print("GETTERS Y SETTERS AGRUPADOS:\n")
auto_get_set(list_of_atts)
print("\n\nGETTERS Y SETTERS ALTERNADOS:\n")
auto_get_set2(list_of_atts)

    
    

    
    
    
    
