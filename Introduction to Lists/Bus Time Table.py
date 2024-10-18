"""
Name : Prabash 
      
"""

def main():
    # Bus schedule in integer format
    bus_schedule = [630, 1015, 1415, 1620, 1720, 2000]

    # Get user input for current time
    current_time = int(input("Enter the time (as an integer): "))

    # Find the index of the next bus or the first bus of the next day
    next_bus_index = 0
    while next_bus_index < len(bus_schedule) and bus_schedule[next_bus_index] < current_time:
        next_bus_index += 1
    if next_bus_index == len(bus_schedule):
        next_bus_index = 0  # Start from the beginning of the schedule if the current time is after the last bus

    # Print the next three bus departure times
    buses_printed = 0
    print("The next buses leave:")
    for i in range(next_bus_index, next_bus_index + 3):
        print(bus_schedule[i % len(bus_schedule)])  # Utilizing remainder operator for circular printing
        buses_printed += 1
        if buses_printed == 3:
            break

if __name__ == "__main__":
    main()

