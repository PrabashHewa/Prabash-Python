"""
Name : Prabash 
       
"""

def main():
    answer = input("Bored? (y/n) ").strip().lower()

    while answer != 'y':
        answer = input("Bored? (y/n) ").strip().lower()

    print("Well, let's stop this, then.")

if __name__ == "__main__":
    main()
