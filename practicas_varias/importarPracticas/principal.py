from funciones_1 import its_prime

print("A continuacion se muestran los numeros primos del 1 al 100")
result = ""

for i in range(100):
    if its_prime(i):
        result = result + str(f"{i}, ")    
print(result)

