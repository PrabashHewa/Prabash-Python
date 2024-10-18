"""
Name : Prabash 
       
"""

def main():
    answer = input("Answer Y or N: ")

    while answer != 'Y' and answer != 'N' and answer != 'y' and answer != 'n':
        print("Incorrect entry.")
        answer = input("Answer Y or N: ")

    if answer == 'Y':
        print("You answered Y")
    elif answer == 'y' :
        print("You answered y")
    elif answer == 'n' :
        print("You answered n")
    else:
        print("You answered N")

if __name__ == "__main__":
    main()
