"""
Name : Prabash 
       
"""

def main():
    
    num = int(input("Choose a number: "))
    
    i = 1
    
    while True :
      
        res = i * num
        print(f"{i} * {num} = {res}")
        
        if res > 100 :
            break
        i += 1
if __name__ == "__main__":
    main()
