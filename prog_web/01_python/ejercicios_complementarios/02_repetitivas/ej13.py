#Un grupo de 100 estudiantes presentan un exámen de Física. Diseñe
#  un diagrama que lea por cada estudiante la calificación obtenida
#  y calcule e imprima:

# A.- La cantidad de estudiantes que obtuvieron una calificación menor
#       a 50.
# B.- La cantidad de estudiantes que obtuvieron una calificación de 50 
#       o más pero menor que 70.
# C.- La cantidad de estudiantes que obtuvieron una calificación de 70 
#       o más pero menor que 80.
# D. La cantidad de estudiantes que obtuvieron una calificación de 80 
#       o más..

x = input("Ingrese la cantidad de estudiantes a evaluar: (no ingrese"
            " nada para indicar una cantidad de 100 estudiantes):\n")
if x == "" or x ==" " or x == "0":
    x = 100
else:
    x = int(x)

print(f"Se deberan ingresar las notas de {x} estudiantes.\n")

cont_A = cont_B = cont_C = cont_D = 0
for i in range(1, x+1):
    print("//////////////////////////////////////////////////////////////////")
    nota = float(input(f"Ingrese la nota del estudiante {i} "
                        "usando valores del 0 al 100: "))
    if nota < 50:
        cont_A += 1
    if 50 <= nota < 70:
        cont_B += 1
    if 70 <= nota < 80:
        cont_C += 1
    if nota >= 80:
        cont_D += 1

print(f"{cont_A} estudiantes tuvieron una calificacion menor a 50.")
print(f"{cont_B} estudiantes tuvieron una calificacion de 50 o más "
        "pero menor que 70.")
print(f"{cont_C} estudiantes tuvieron una calificacion de 70 o más "
        "pero menor que 80.")
print(f"{cont_D} estudiantes tuvieron una calificacion de 80 o más.")