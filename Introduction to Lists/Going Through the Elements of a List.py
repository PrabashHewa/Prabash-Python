"""
Name : Prabash 
      
"""
def main():
# Initialize an empty list to store user input
 numbers = []

# Ask the user to enter 5 numbers
 print("Give 5 numbers:")
 for i in range(5):
    num = float(input("Next number: "))
    numbers.append(num)

# Print the numbers greater than zero
 print("The numbers you entered that were greater than zero were:")
 for num in numbers:
    if num > 0:
        print(int(num))


    
    
if __name__ == "__main__":
    main()

