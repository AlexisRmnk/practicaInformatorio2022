# Realizar un programa que sea capaz de, 
# habiéndose ingresado dos números m y n, determine si n es divisor de m.

m = int(input("Ingrese un numero entero 'm'\n"))
n = int(input("Ingrese un numero entero 'n'\n"))

if (m%n == 0):
    print(f"{m} es divisible por {n} y su division devuelve "
            f"{round(m/n, 2)} con resto {m%n}. "
            f"Es decir, {n} ES DIVISOR de {m}")
else: 
    print(f"{m} NO es divisible por {n} y su division devuelve "
            f"{round(m/n, 2)} con resto {m%n}. "
            f"Es decir, {n} NO ES DIVISOR de {m}")