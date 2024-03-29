# autogetter y setter for python
# author: Alexis Romaniuk

def first_letter_uppercase(string_:str) -> str:
    '''reemplazo de string_.capitalize'''
    return string_[0].upper() + string_[1:]

def getter_ (atribute_:str, is_private:bool = False):
    if is_private:
        return f'''def get{first_letter_uppercase(atribute_)}(self):
    return self.__{atribute_}'''
    else:
        return f'''def get{first_letter_uppercase(atribute_)}(self):
    return self.{atribute_}'''
    
def setter_ (atribute_:str, is_private:bool = False):
    if is_private: 
        return f'''def set{first_letter_uppercase(atribute_)}(self, {atribute_}):
    self.__{atribute_} = {atribute_}'''
    else:
        return f'''def set{first_letter_uppercase(atribute_)}(self, {atribute_}):
    self.{atribute_} = {atribute_}'''

def list_atts():
    print(("\nIngresar cadenas con atributos ('ENTER' para ingresar"
           " siguiente atributo, '0' para finalizar carga de atributos)."
            "\nFormato de Ejemplo: 'atributo1' (se permiten guiones "
            "bajos '_')\n\t"))
    list_of_atts = list()
    i = 1
    while(True):
        print(f"ATRIBUTO {i}:")
        string_ = input("\t")
        string_.strip()
        if string_ == "0":
            print("Finalizando carga de atributos\n")
            break
        if not string_.replace("_","").isalnum():
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
        
def auto_get_setV2(list_of_atts_:list):
    for att in list_of_atts_:
        print(getter_(att, True))
    print("")
    for att in list_of_atts_:
        print(setter_(att, True)) 
def auto_get_set2V2(list_of_atts_:list):
    for att in list_of_atts_:
        print(getter_(att, True))
        print(setter_(att, True))