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
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

def main():
    print("Enter fractions in the format integer/integer.")
    print("One fraction per line. Stop by entering an empty line.")

    fractions = []

    while True:
        fraction_str = input().strip()
        if not fraction_str:  # Stop if an empty line is entered
            break
        
        numerator, denominator = map(int, fraction_str.split('/'))
        fraction = Fraction(numerator, denominator)
        fractions.append((fraction_str, fraction))
    
    print("The given fractions in their simplified form:")
    for fraction_str, fraction in fractions:
        fraction.simplify()
        print(f"{fraction_str} = {fraction}")

if __name__ == "__main__":
    main()



