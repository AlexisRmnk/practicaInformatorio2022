class Uno:
    def metod(self):
        return 1 + 1
    
class Dos(Uno):
    def metod(self):
        return super().metod() + 1
    
d = Dos()

print(d.metod())

