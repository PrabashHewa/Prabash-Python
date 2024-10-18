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
    
    def __lt__(self, other):
        common_denominator = self.denominator * other.denominator
        numerator1 = self.numerator * other.denominator
        numerator2 = other.numerator * self.denominator
        return numerator1 < numerator2
    
    def __gt__(self, other):
        common_denominator = self.denominator * other.denominator
        numerator1 = self.numerator * other.denominator
        numerator2 = other.numerator * self.denominator
        return numerator1 > numerator2

# Example usage:
frac1 = Fraction(1, 2)
frac2 = Fraction(2, 3)

print(f"Is frac1 < frac2? {frac1 < frac2}")
print(f"Is frac1 > frac2? {frac1 > frac2}")




