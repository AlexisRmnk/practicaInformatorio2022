class Triangle:
    def __init__(self, s1, s2, s3):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
    
    def getSide1(self):
        return self.side1
    def getSide2(self):
        return self.side2
    def getSide3(self):
        return self.side3

    def setSide1(self, side1):
        self.side1 = side1
    def setSide2(self, side2):
        self.side2 = side2
    def setSide3(self, side3):
        self.side3 = side3

    def type(self):
        s1 = self.side1
        s2 = self.side2
        s3 = self.side3
        list_ = [s1, s2, s3]        
        list_.sort()
        s1, s2, s3 = list_
        #print(f"\nTEST: El lado mayor tiene {list_[2]} cm.")
        if s1 == s2 == s3:
            print("El triangulo es equilatero.")
            print(f"Todos los lados miden {s1} cm.")
        elif (list_.count(s1) == 2):
            print("El triangulo es isosceles.")
            print(f"El lado mayor tiene {list_[2]} cm.")
        elif (list_.count(s3) == 2):
            print("El triangulo es isosceles.")
            print(f"Los dos lados mayores tienen {list_[2]} cm.")
        else:
            print("El triangulo es escaleno")
            print(f"El lado mayor tiene {list_[2]} cm.")