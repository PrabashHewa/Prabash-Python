"""
Name : Prabash 
      
"""

def main():
 def official_score(times):
   """ Remove the best and worst times """
   times.remove(min(times))
   times.remove(max(times))
    
   average_time = sum(times) / len(times)
   return round(average_time, 2)


 performance_times = []
 for i in range(1, 6):
    time = float(input(f"Enter the time for performance {i}: "))
    performance_times.append(time)


 official_time = official_score(performance_times)
 print(f"The official competition score is {official_time} seconds.")

if __name__ == "__main__":
    main()
