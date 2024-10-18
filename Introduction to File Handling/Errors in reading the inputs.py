"""
Name : Prabash 
      
"""

def read_input(prompt):
    ''' function that checks for incorrect entries and asks the user to input again until a valid integer is entered'''
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
       

def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    
    print()
    # Printing the frame
    for _ in range(height):
        
        print(mark * width)

if __name__ == "__main__":
    main()



