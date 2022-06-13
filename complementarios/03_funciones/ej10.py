# Ejercicio 10: Precedencia del operador
# Escriba una función llamada precedencia que devuelve un número entero
#  que representa la precedencia de un operador matemático. Una cadena
#  que contiene el operador se pasará a la función como su único parámetro.
#  Su función debe devolver 1 para + y -, 2 para * y /, y 3 para ^.
#  Si la cadena que se pasa a la función no es uno de estos operadores,
#  la función debería devolver -1. Incluya un programa principal que
#  lea un operador del usuario y muestre la precedencia del operador o
#  un mensaje de error que indique que la entrada no era un operador.

# En este ejercicio, se usa ˆ para representar la exponenciación, en
#  lugar de la elección de Python de **, para facilitar el desarrollo
#  de la solución.

def precedencia(string_):
    string_ = string_.strip()
    if (len(string_) != 1):
        return -1
    else:
        if string_ == "-" or string_ == "+":
            return 1
        elif string_ == "*" or string_ == "/":
            return 2
        elif string_ == "^" or string_ == "ˆ":
            return 3
        else:
            return -1

print("Indique el signo de la operacion para conocer su precedencia:"
        "\n\t+\t-\t*\t/\t^ (ALT + 94)")
x = input("\t")
operator_precedence = precedencia(x)
if operator_precedence != -1:
    print(f"La precedencia del codigo es {operator_precedence}")
else:
    print("Error - la entrada no era un operador!")