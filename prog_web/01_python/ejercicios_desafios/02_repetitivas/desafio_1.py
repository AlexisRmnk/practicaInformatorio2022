# https://sites.google.com/view/nivel1-desafios/repetitivas
# desafio 1

print("Primer login (user:admin pass: 123)")

# bandera = True
# while(bandera):
#     user = input("Ingresar nombre de usuario: ")
#     password = input("Ingresar contraseña: ")
#     if (user == "admin" and password == "123"):
#         bandera = False

while(True):
    user = input("Ingresar nombre de usuario: ")
    password = input("Ingresar contraseña: ")
    if (user == "admin" and password == "123"):
        break
    print("Credenciales incorrectas! Reintentar.\n")   

print("Primer login ejecutado\n---------------------------------------\n")
print("Segundo login (user:root pass: abc)")

bandera = False
print("Ingresar usuario y contraseña. Intentos: 3")
for i in range(3):
    user = input("Ingresar nombre de usuario: ")
    password = input("Ingresar contraseña: ")
    if (user == "root" and password == "abc"):
        bandera = True
        break
    else:
        print(f"No valido. {2-i} intentos restantes.")

if (bandera):
    print("ACCESO CONCEDIDO")
else: 
    print("ACCESO DENEGADO")