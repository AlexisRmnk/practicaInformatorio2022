# Programa que pide la pass y solo hay 5 intentos.
bandera = False

for i in range(5):
    print("Ingrese la contraseña para el usuario Fulanito:")
    password = input("Contraseña: ")
    if password=="123":
        bandera = True
        break
    else: 
        print(f"Intento {i+1} fallido. Intentos restantes: {4-i}")

if (bandera): # (not bandera):
    print("Acceso permitido")
else:
    print("Cuenta bloqueada")