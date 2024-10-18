"""
Name : Prabash 
      
"""

def read_message():
    '''Function to read user message until an empty line is entered'''
    message = []
    while True:
        line = input()
        if line.strip():  # Check if the line is not empty
            message.append(line)
        else:
            break
    return message

def main():
    filename = input("Enter the name of the file: ")

    try:
        # Opening the file for writing
        with open(filename, 'w') as file:
            print("Enter rows of text. Quit by entering an empty row.")
            # Reading user message
            message = read_message()

            # Writing message to file with line numbers
            for i, line in enumerate(message, 1):
                file.write(f"{i} {line}\n")

        print(f"File {filename} has been written.")

    except FileNotFoundError:
        print(f"Writing the file {filename} was not successful.")

    except PermissionError:
        print(f"Writing the file {filename} was not authorized.")

if __name__ == "__main__":
    main()





