"""
Name : Prabash 
      
"""
def main():

 numbers = []


 print("Give 5 numbers:")
 for i in range(5):
    num = int(input("Next number: "))
    numbers.append(num)


 print("The numbers you entered, in reverse order:")
 for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i])


if __name__ == "__main__":
    main()

