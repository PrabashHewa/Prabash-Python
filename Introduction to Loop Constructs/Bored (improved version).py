"""
Name : Prabash 
      
"""

def main():
 while True:
    bored_response = input("Bored? (y/n) ").lower()
    if bored_response == 'y':
        print("Well, let's stop this, then.")
        break
    elif bored_response == 'n':
        while True:
            bored_response = input("Bored? (y/n) ").lower()
            if bored_response == 'y':
                print("Well, let's stop this, then.")
                break
            elif bored_response == 'n':
                continue
            else:
                print("Incorrect entry.")
                continue
        break  
    else:
        print("Incorrect entry.")
        continue


if __name__ == "__main__":
    main()
