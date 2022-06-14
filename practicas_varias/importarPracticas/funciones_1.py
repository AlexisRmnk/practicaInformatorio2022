def its_prime(number_):
    if number_ < 2:
        return False
    for n in range(2, number_):
        if number_%n == 0:
            return False
    return True

if __name__ == '__main__':
    print("ESTO SOLO SE IMPRIME SI SE EJECUTA DIRECTAMENTE funciones.py")

print("****** Esto SI se imprime si se importa desde cualquier otro programa. ******")