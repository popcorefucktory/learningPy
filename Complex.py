# вывод комплексного числа

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.x = real
        self.y = imaginary
    def __str__(self):
        return str(self.x) + (self.y >= 0 and " +" or " ") + str(self.y) + "i"

Number1 = ComplexNumber(3, -8)


#  z1 = a1 + b1i  z2 = a2 + b2i  z = (a1 + a2) + (b1 + b2)i








