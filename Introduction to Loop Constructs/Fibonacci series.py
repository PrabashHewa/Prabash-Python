"""
Name : Prabash 
      
"""

def main():
    num_times = int(input("How many Fibonacci numbers do you want? "))

    previous_fib = 1
    current_fib = 1

    print(f"1. {previous_fib}")
    if num_times > 1:
        print(f"2. {current_fib}")

    for i in range(3, num_times + 1):
        next_fib = previous_fib + current_fib
        print(f"{i}. {next_fib}")

        previous_fib, current_fib = current_fib, next_fib

if __name__ == "__main__":
    main()
