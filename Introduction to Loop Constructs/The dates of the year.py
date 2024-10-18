"""
Name : Prabash 
      
"""

def main():
 days_in_month = {
    1.: 31,  
    2.: 28,  
    3.: 31,  
    4.: 30,  
    5.: 31,  
    6.: 30,  
    7.: 31, 
    8.: 31,  
    9.: 30,  
    10.: 31, 
    11.: 30, 
    12.: 31  
}


 for month in range(1, 13):
    
    for day in range(1, days_in_month[month] + 1):
        print(day, ".", month, ".", sep="")



if __name__ == "__main__":
    main()
