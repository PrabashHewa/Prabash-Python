"""
Project: Weather Statistics
This program collects temperature data for a specified number of days and then 
calculates the mean and median temperatures. The program classifies days into
those with temperatures above or below the median as an ouput.

Author: Prabash
"""

def calculate_mean(temperatures):
    """
    Calculate the mean temperature.

    Parameters:
    temperatures : List of temperature readings.

    Returns: The mean of the temperature readings.
    """
    total = sum(temperatures)
    count = len(temperatures)
    return total / count

def calculate_median(temperatures):
    """
    Calculate the median temperature.

    Parameters:
    temperatures : List of temperature readings.

    Returns: The median of the temperature readings.
    """
    sorted_temps = sorted(temperatures)
    n = len(sorted_temps)
    mid = n // 2
    if n % 2 == 1:
        return sorted_temps[mid]
    else:
        return (sorted_temps[mid - 1] + sorted_temps[mid]) / 2

def classify_temperatures(temperatures, median_temp):
    """
    Classify days into those with temperatures above or at the median,
    and those below the median.

    Parameters:
    temperatures : List of temperature readings.
    median_temp : The median temperature.

    Returns:  
    The first list contains days with temperatures above or at the median 
    second list contains days with temperatures below the median. 
    Each tuple contains the day number, temperature, and difference to mean.
    """
    above_or_at_median = []
    below_median = []
    for i, temp in enumerate(temperatures, 1):
        if temp >= median_temp:
            above_or_at_median.append(i)
        else:
            below_median.append(i)
    return above_or_at_median, below_median

def print_results(days, temperatures, mean_temp, header):
    """
    Print the results for the classified days.

    Parameters:
    days : List of day numbers.
    temperatures : List of temperature readings.
    mean_temp : The mean temperature.
    header : The header to print before the results.

    """
    print(header)
    for day in days:
        temp = temperatures[day - 1]
        diff = temp - mean_temp
        print(f"Day {day:2}. {temp:5.1f}C difference to mean: {diff:5.1f}C")

def main():
    """
    Main function to run the temperature analyzer program.
    """
    num_days = int(input("Enter amount of days: "))
    temperatures = []

    for i in range(1, num_days + 1):
        temp = float(input(f"Enter day {i}. temperature in Celsius: "))
        temperatures.append(temp)

    mean_temp = calculate_mean(temperatures)
    median_temp = calculate_median(temperatures)

    print(f"\nTemperature mean: {mean_temp:.1f}C")
    print(f"Temperature median: {median_temp:.1f}C")

    above_or_at_median, below_median = classify_temperatures(temperatures, median_temp)

    print_results(above_or_at_median, temperatures, mean_temp, "\nOver or at median were:")
    print_results(below_median, temperatures, mean_temp, "\nUnder median were:")

if __name__ == "__main__":
    main()
