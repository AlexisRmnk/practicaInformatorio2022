# MOSTRAR MENSAJE POR PANTALLA
print("Test")
variable = "cadena de txt"
treinta = 30
print("Variable = ", variable, " . Treinta = ", treinta,".")

comillas_simple = "lorem impsun"
print("Test de comillas simples '", comillas_simple, "'")

comillas_dobles = 'lorem impsun'
print('Test de comillas dobles "', comillas_dobles, '"')

print("prueba de input")

nombre = input("INGRESE SU NOMBRE: ")
edad = input("INGRESE SU EDAD: ")

print("Ud se llama ", nombre, " y tiene ", edad," años. (test sin SEP")
print("Ud se llama ", nombre, " y tiene ", edad," años. (test con SEP", sep="")
# SEP sirve para indicar con que se separan las cadenas de texto de las 
# variables en el print
print("Ud se llama ", nombre, "y tiene ", edad," años."
    "(test2 con SEP.", sep="XxX")