class ImaginaryNumber:
    def __init__(self, real = 0, imaginary = 0):
        self.a = real
        self.b = imaginary
    
    def getRealPart(self):
        return self.a
    
    def getImaginaryPart(self):
        return self.b

    def setRealPart(self, real):
        self.a = real

    def setImaginaryPart(self, imaginary):
        self.a = imaginary
        
    def __str__(self):
        if self.b == 0:
            return str(self.a)
        
        sign = ''
        real = ''
        if self.a != 0:
            real = str(self.a)
        if self.a != 0 and self.b > 0:
            sign = '+'
        
        return real + sign + str(self.b) + 'i'

    def __mul__(self, other):
        """
        Multiply 2 complex numbers using 3 multiplications of 
        real numbers and more additions and subtractions
        Using Karatsuba algorithm
        (self.a + self.b * i)(other.a + other.b * i)
        """
        p1 = self.a * other.a
        p2 = self.b * other.b
        p3 = (self.a + self.b) * (other.a + other.b)
        return ImaginaryNumber(p1 - p2, p3 - p2 - p1)

    __rmul__ = __mul__

a = ImaginaryNumber(2, 1)
b = ImaginaryNumber(3, -2)
print(a * b, "=", "8+1i")