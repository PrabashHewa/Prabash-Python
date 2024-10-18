"""
Name : Prabash 
      
"""

def generate_cheat_sheet(max_numbers):
    
    """ 
genratae cheat sheet function is checking wherther number i is divisiable by
3 or 7 or both numbers. According to divisablity it is assaing zip, boing or zip-boing.
Then this print the numbers and it is return in main fucntion
    """
    for i in range(1, max_numbers + 1):
        if i % 3 == 0 and i % 7 == 0: #  Check divisible by both the numbers
            print("zip boing")
        elif i % 3 == 0:  # Check divisible by number 3
            print("zip")
        elif i % 7 == 0:  # Check divisible by number 7
            print("boing")
        else:
            print(i)   # Printing numbers 

def main():
   
        max_numbers = int(input("How many numbers would you like to have? "))
    
        generate_cheat_sheet(max_numbers) # Returning number and zip boing
  

if __name__ == "__main__":
    main()
