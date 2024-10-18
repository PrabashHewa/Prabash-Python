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
    
    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        result = Fraction(new_numerator, new_denominator)
        result.simplify()
        return result
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

def add_fraction(calculator):
    """Add a fraction to the calculator's memory."""
    while True:
        fraction_input = input("Enter a fraction in the form integer/integer: ").strip()
        try:
            numerator, denominator = map(int, fraction_input.split('/'))
            fraction = Fraction(numerator, denominator)
            break
        except ValueError:
            print("Invalid input format. Please enter the fraction in the form integer/integer.")
    name = input("Enter a name: ")
    calculator[name] = fraction

def print_fraction(calculator):
    """Print a fraction from the calculator's memory."""
    name = input("Enter a name: ")
    fraction = calculator.get(name)
    if fraction:
        print(f"{name} = {fraction}")
    else:
        print(f"Name {name} was not found")

def list_fractions(calculator):
    """List all fractions in the calculator's memory."""
    if calculator:
        sorted_names = sorted(calculator.keys())
        for name in sorted_names:
            print(f"{name} = {calculator[name]}")
    else:
        print("Calculator's memory is empty.")

def multiply_fractions(calculator):
    """Multiply two fractions from the calculator's memory."""
    first_operand = input("1st operand: ")
    second_operand = input("2nd operand: ")
    if first_operand in calculator and second_operand in calculator:
        result = calculator[first_operand] * calculator[second_operand]
        print(f"{calculator[first_operand]} * {calculator[second_operand]} = {result.numerator}/{result.denominator}")
        print(f"simplified {result}")
    else:
        print("One or both operands not found")

def read_file(calculator):
    """Read fractions from a file and save them to the calculator's memory."""
    file_name = input("Enter the name of the file: ")
    try:
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()
                if "=" in line:
                    name, fraction_str = line.split("=")
                    try:
                        numerator, denominator = map(int, fraction_str.split('/'))
                        fraction = Fraction(numerator, denominator)
                        calculator[name.strip()] = fraction
                    except ValueError:
                        print(f"Error: Invalid fraction format in line: {line}")
                else:
                    print(f"Error: Invalid format in line: {line}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' cannot be read.")

def main():
    calculator = {}
    
    while True:
        command = input("> ").strip()
        if command == "quit":
            print("Bye bye!")
            break
        elif command == "add":
            add_fraction(calculator)
        elif command == "print":
            print_fraction(calculator)
        elif command == "list":
            list_fractions(calculator)
        elif command == "*":
            multiply_fractions(calculator)
        elif command == "file":
            read_file(calculator)
        else:
            print("Unknown command!")

if __name__ == "__main__":
    main()
