"""
Name : Prabash 
       
"""

def main():
    
    num = int(input("Choose a number: "))
    
    for i  in range (1,11) :
        res = i * num
        print(f"{i} * {num} = {res}")
        
if __name__ == "__main__":
    main()
