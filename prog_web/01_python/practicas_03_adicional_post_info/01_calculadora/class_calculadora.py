from decimal import Decimal

class Calculadora:
    current_value = 0.0

    def __format_float(self, input_):
        '''try to return an integer version of the input if it can'''
        input_ = Decimal(str(input_))
        if input_ == input_.to_integral_value():
            return int(input_)
        else:
            return input_

    def show_status(self):
        print(f"El valor actual es: {self.__format_float(self.current_value)}")
    
    def suma(self):
        print("Introduce el valor a sumar:")
        valor = self.__check_number()
        self.current_value += valor
        self.show_status()

    def resta(self):
        print("Introduce el valor a restar:")
        valor = self.__check_number()
        self.current_value -= valor
        self.show_status()

    def multiplicacion(self):
        print("Introduce el valor a multiplicar:")
        valor = self.__check_number()
        self.current_value *= valor
        self.show_status()

    def division(self):
        while(True):
            print("Introduce el valor a dividir por:")
            valor = self.__check_number()
            if valor == 0:
                print("Error. No se puede dividir por 0! Reingresar.")
                continue
            self.current_value /= valor
            self.show_status()
            break
    
    def div_ent_y_resto(self):
        while(True):
            print("Introduce el valor a dividir por (div entera):")
            valor = self.__check_number()
            if valor == 0:
                print("Error. No se puede dividir por 0! Reingresar.")
                continue
            aux_remainder = self.current_value % valor
            self.current_value //= valor
            self.show_status()
            print(f"Resto de division entera: {aux_remainder}")
            break

    def potencia(self):
        print("Introduce el valor del exponente a elevar:")
        valor = self.__check_number()
        self.current_value **= valor
        self.show_status()

    def resetear_valor(self):
        self.current_value = 0.0
        self.show_status
    
    def raiz(self):
        while(True):
            print("Introduce el valor del exponente de la raiz :")
            valor = self.__check_number()
            if valor == 0:
                print("Error. No puede ser 0! Reingresar.")
                continue
            self.current_value **= (1/valor)
            self.show_status()
            break
    
    def __check_number(self):
        '''Checkea que el input sea numerico'''
        string_ = input()
        while(True):
            try:
                float_ = float(string_)
                break
            except:
                print("Valor erroneo.")
                float_ = input("Ingrese un valor correcto: ")
                continue
        return float_
