from class_calculadora import Calculadora

def input_integer():
	'''Solicita que se ingrese un entero. 
		Solo sale de la funcion si se ingresa un numero entero'''
	
	string_ = input()
	while(True):
		try:
			integer_=int(string_)
			break
		except:
			print("Valor erroneo.")
			integer_ = input("Ingrese un valor correcto: ")
			continue
	return integer_

	
def menu():
	calc = Calculadora()
 
	while(True):
		options = {1:"SUMA", 2:"RESTA", 3:"MULTIPLICACION", 4:"DIVISION",
			 5:"DIVISION ENTERA Y RESTO", 6:"POTENCIA", 7:"RAIZ",
			 8:"VER TOTAL", 0:"RESETEAR VALOR", -1:"SALIR"}
		
		print("\n#######################################\n"
			"#######################################\n")
		
		print("A continuacion ingrese la accion que desea realizar: ")
		
		print("#######################################")
		for (key, value) in options.items():
			print("{:<30} {:<15}".format(f"Para {value}", f"ingresar {key}"))
		print("#######################################")
			
		accion = input_integer()

		if accion not in options.keys():
			print("La accion no se encuentra entre las opciones validas."
				  " Reingresar valor.")
			continue
		elif(accion == -1):
			print("Saliendo de la calculadora.")
			break
		elif(accion == 0):
			calc.resetear_valor()
		elif(accion == 1):
			calc.suma()
		elif(accion == 2):
			calc.resta()
		elif(accion == 3):
			calc.multiplicacion()
		elif(accion == 4): 
			calc.division()
		elif(accion == 5):
			calc.div_ent_y_resto()
		elif(accion == 6):
			calc.potencia()
		elif(accion == 7):
			calc.raiz()
		elif(accion == 8):
			calc.show_status()
		else:
			print("El valor introducido no es correcto. Reintentar.")
  
