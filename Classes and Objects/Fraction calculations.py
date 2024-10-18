"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions code template
"""

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def simplify(self):
        common = self.gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator //= common
    
    def return_string(self):
        return f"{self.numerator}/{self.denominator}"
    
    def multiply(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def reciprocal(self):
        return Fraction(self.denominator, self.numerator)
    
    def divide(self, other):
        reciprocal_other = other.reciprocal()
        return self.multiply(reciprocal_other)
    
    def add(self, other):
        new_denominator = self.denominator * other.denominator
        new_numerator1 = self.numerator * other.denominator
        new_numerator2 = other.numerator * self.denominator
        return Fraction(new_numerator1 + new_numerator2, new_denominator)
    
    def deduct(self, other):
        new_denominator = self.denominator * other.denominator
        new_numerator1 = self.numerator * other.denominator
        new_numerator2 = other.numerator * self.denominator
        return Fraction(new_numerator1 - new_numerator2, new_denominator)

# Example usage:
frac1 = Fraction(5, 7)
frac2 = Fraction(3, 8)

# Addition
sum_result = frac1.add(frac2)
print(f"Sum: {sum_result.return_string()}")
sum_result.simplify()
print(f"Simplified Sum: {sum_result.return_string()}")

# Subtraction
difference_result = frac1.deduct(frac2)
print(f"Difference: {difference_result.return_string()}")
difference_result.simplify()
print(f"Simplified Difference: {difference_result.return_string()}")



