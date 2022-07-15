# Ejercicio 12: Próximo Siguiente
# En este ejercicio creará una función llamada proximo_primo que
#  encuentra y devuelve el primer número primo mayor que algún número
#  entero, n. El valor de n se pasará a la función como su único
#  parámetro. Incluya un programa principal que lea un número entero
#  del usuario y muestre el primer número primo mayor que el valor ingresado.

#funcion del ej 11
def its_prime(number_):
    if number_ < 2:
        return False
    for n in range(2, number_):
        if number_%n == 0:
            return False
    return True

def proximo_primo(num):
    while(True):
        num += 1
        if (its_prime(num)):
            break
    return num

print("Ingrese un numero:")
x = int(input("\t"))

next_prime_number = proximo_primo(x)
print(f"El proximo numero que sera primo despues del {x} es el"
        f" {next_prime_number}")