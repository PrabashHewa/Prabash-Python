"""
COMP.CS.100 Programming 1
Print a box with input error checking
"""
def print_box(width, height, mark):
    """
 This function Takes a prompt string as a parameter. 
 Checks if the number is greater than zero. If it is, it returns the number.
"""
    for _ in range(height):
        print(mark * width)

def read_input(prompt):
    """
This function reads a user input, checks if it's greater than zero, 
and prompts the user until they provide a valid input
"""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass
            
def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
