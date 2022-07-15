# Ejercicio 9: ¿Un string representan un entero?
# En este ejercicio escribirá una función llamada es_entero que determina
#  si los caracteres en una cadena representan un número entero válido.
#  Al determinar si un string representa un número entero, debe ignorar
#  cualquier espacio en blanco inicial o final. Una vez que se ignora
#  este espacio en blanco, una cadena representa un número entero si su
#  longitud es al menos 1 y solo contiene dígitos, o si su primer carácter
#  es + o - y el primer carácter va seguido de uno o más caracteres, todos
#  los cuales son dígitos Escriba un programa principal que lea una cadena
#  del usuario e informe si representa o no un número entero.

# Sugerencia: Puede encontrar los métodos lstrip, rstrip y / o strip para
#  cadenas útiles cuando complete este ejercicio.

# notas:
#   strip remueve espacios iniciales y finales en la cadena. txt.strip()
#       lstrip() y rstrip() sirven de forma similar, IZQ y DER

def es_entero(string_):
    string_ = string_.strip()
    if (len(string_) < 1):
        return False
    else:
        flag = True #first element indicator
        for char_ in string_:
            if char_ == "+" and flag:
                if len(string_) == 1:
                    return False
                flag = False
                continue
            elif char_ == "-" and flag:
                if len(string_) == 1:
                    return False
                flag = False
                continue
            else:
                if (char_ == "0" or char_ == "1" or char_ == "2" 
                   or char_ == "3" or char_ == "4" or char_ == "5"  
                   or char_ == "6" or char_ == "7" or char_ == "8" 
                   or char_ == "9"):
                    if flag:
                        flag = False
                    continue
                else:
                    return False
    return True

print("Ingrese un numero entero sin espacios "
        "(puede incluir el signo al comienzo):")
x = input("\t")

if es_entero(x):
    print("El valor ingresado es un numero entero. Bien hecho!")
else:
    print("El valor ingresado NO es un numero entero.")