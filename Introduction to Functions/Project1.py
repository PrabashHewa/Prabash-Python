"""
Name : Prabash 
      
"""


def main():
    days = int(input("Enter the number of days: "))
    
    distances = []
    consecutive_zeros = 0
    
    for i in range(1, days + 1):
        distance = float(input(f"Enter day {i} running length: "))
        distances.append(distance)

        if distance == 0:
            consecutive_zeros += 1
        else:
            consecutive_zeros = 0
        
        if consecutive_zeros >= 3:
            print()
            print("You had too many consecutive lazy days!")
            return
    
    mean_distance = sum(distances) / days
    
    print()
    if mean_distance < 3.00:
        print(f"Your running mean of {mean_distance:.2f} km was too low!")
    else:
        print(f"You were persistent runner! With a mean of {mean_distance:.2f} km.")
    
    
if __name__ == "__main__":
    main()
