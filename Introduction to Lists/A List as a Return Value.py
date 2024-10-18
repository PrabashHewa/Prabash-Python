"""
Name : Prabash 
      
"""
def input_to_list(num_integers):
    """Function to read 'num_integers' numbers fro6m user input and return them in a list."""
    numbers = []
    print(f"Enter {num_integers} numbers:")
    for _ in range(num_integers):
        num = int(input())
        numbers.append(num)
    return numbers

def main():
    num_to_process = int(input("How many numbers do you want to process: "))
    numbers_list = input_to_list(num_to_process)
    search_number = int(input("Enter the number to be searched: "))
    
    count = numbers_list.count(search_number)
    if count > 0:
        print(f"{search_number} shows up {count} times among the numbers you have entered.")
    else:
        print(f"{search_number} is not among the numbers you have entered.")

if __name__ == "__main__":
    main()

