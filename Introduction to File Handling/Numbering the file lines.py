"""
Name : Prabash 
      
"""

def main():
    filename = input("Enter the name of the file: ")

    try:
        with open(filename, 'r') as file:
            row_number = 1
            for line in file:
                line = line.rstrip()
                print(f"{row_number} {line}")
                row_number += 1

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == "__main__":
    main()







