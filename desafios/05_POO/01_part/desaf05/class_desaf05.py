class Tiempo:
    def __init__(self, hour, minute = 0, second = 0):
        self.time_validation(hour, minute, second)
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        
    def __str__(self) -> str:
        if self.__hour < 10:
            hour_str = "0" + str(self.__hour)
        else: 
            hour_str = str(self.__hour)
        if self.__minute < 10:
            minute_str = "0" + str(self.__minute)
        else: 
            minute_str = str(self.__minute)
        if self.__second < 10:
            second_str = "0" + str(self.__second)
        else: 
            second_str = str(self.__second)
        
        return (f"Hora:    {self.__hour}\nMinuto:  {self.__minute}\nSegundo:"
                f" {self.__second}\n\t({hour_str}:{minute_str}:"
                f"{second_str} HS)")
    
    def time_validation(self, hour, minute, second):
        if not isinstance(hour, int):
            raise ValueError("La hora debe ser un valor entero.")
        if not isinstance(minute, int):
            raise ValueError("El minuto debe ser un valor entero.")
        if not isinstance(second, int):
            raise ValueError("El segundo debe ser un valor entero.")
        if not 0 <= hour < 24:
            raise ValueError("Error. La hora debe ser un valor entre 0 y 23")
        if not 0 <= minute < 60:
            raise ValueError("Error. El minuto debe ser un valor entre 0 y 59")
        if not 0 <= second < 60:
            raise ValueError("Error. El segundo debe ser un valor entre 0 y 59")

    def modify_time(self, hour, minute = 0, second = 0):
        self.time_validation(hour, minute, second)
        self.__hour = hour
        self.__minute = minute
        self.__second = second        

    def getHour(self):
        return self.__hour
    def setHour(self, hour):
        self.__hour = hour
    def getMinute(self):
        return self.__minute
    def setMinute(self, minute):
        self.__minute = minute
    def getSecond(self):
        return self.__second
    def setSecond(self, second):
        self.__second = second

class PruebaTiempo:
    def __init__(self):
        self.time = Tiempo(0)

    def __menu(self):
        while(True):
            try:
                print("Seleccionar operacion: Modificar Hora (1) - Salir (0)")
                op = int(input("\t"))
                if op in (1, 0):
                    return op
                else:
                    print("Numero invalido!")
                    continue
            except:
                print("Caracter invalido!")
                continue
    
    def ask_hour(self):
        while(True):
            try:
                hour = int(input("Ingrese la hora: (valor"
                                 " entero entre 0 y 23)\n\t"))
                if not (0 <= hour < 24):
                    print("La hora debe estar comprendida entre 0 y 23")
                    continue
                else:
                    return hour
            except:
                print("Valor invalido. Reintentar.")
                continue
   
    def ask_minute(self):         
        while(True):
            try:
                minute = int(input("Ingrese el minuto: (valor"
                                 " entero entre 0 y 60)\n\t"))
                if not (0 <= minute < 60):
                    print("El minuto debe estar comprendido entre 0 y 60")
                    continue
                else:
                    return minute
            except:
                print("Valor invalido. Reintentar.")
                continue
            
    def ask_second(self):        
        while(True):
            try:
                second = int(input("Ingrese el segundo: (valor"
                                 " entero entre 0 y 60)\n\t"))
                if not (0 <= second < 60):
                    print("El segundo debe estar comprendido entre 0 y 60")
                    continue
                else:
                    return second
            except:
                print("Valor invalido. Reintentar.")
                continue

    def mod_time(self):
        print("Indique elementos a modificar:\n\t'ENTER' para modificar todo"
              f"\n\t'Y' para modificar a eleccion (hora, minuto, segundo)")
        x = input("\t").upper().strip()
        if x != "Y":
            hour = self.ask_hour()
            minute = self.ask_minute()
            second = self.ask_second()
        else:            
            print("Desea modificar la hora? 'ENTER' para SI, 'N' para NO")
            x = input("\t").upper().strip()
            if x != 'N':
                hour = self.ask_hour()
            else:
                hour = self.time.getHour()
            print("Desea modificar el minuto? 'ENTER' para SI, 'N' para NO")
            x = input("\t").upper().strip()
            if x != 'N':
                minute = self.ask_minute()
            else:
                minute = self.time.getMinute()
            print("Desea modificar el segundo? 'ENTER' para SI, 'N' para NO")
            x = input("\t").upper().strip()
            if x != 'N':
                second = self.ask_second()
            else:
                second = self.time.getSecond()
        self.time.modify_time(hour, minute, second)
    
    def test(self):
        while(True):
            print(self.time)
            op = self.__menu()
            if op == 0:
                print("Finalizando pruebas")
                break
            else:
                self.mod_time()