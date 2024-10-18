"""
Name : Prabash 
      
"""
def main():
    day = 3
    month = 1
    year = 2014
    
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    while year == 2014:
        print(f"{day}.{month}.")
        day += 7

        if day > days_in_month[month - 1]:
            day -= days_in_month[month - 1]
            month += 1

        if month > 12:
            year += 1
            month = 1

if __name__ == "__main__":
    main()
