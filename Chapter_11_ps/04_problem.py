class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return complex(real_part, imag_part)
 
    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return complex(real_part, imag_part)
# implementing the __str__ method to provide a string representation of the complex number
    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __len__(self):
        return 2  # A complex number has two components: real and imaginary
    
c1 = complex(2, 3)
c2 = complex(1, 4)

print(c1 + c2)  # Addition
print(c1 - c2)  # Subtraction

print(c1 * c2)  # Multiplication
print(c1 / c2)  # Division  

print(len(c1))  # Length of the complex number

