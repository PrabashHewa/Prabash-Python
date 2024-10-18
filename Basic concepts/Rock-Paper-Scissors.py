def main():
    
    Pl1 = input("Player 1, enter your choice (R/P/S): ")
    Pl2 = input("Player 2, enter your choice (R/P/S): ")
  
    if Pl1 == Pl2 :
        print("It's a tie!")
    elif (Pl1 == 'R' and Pl2 == 'S') or \
         (Pl1 == 'S' and Pl2 == 'P') or \
         (Pl1 == 'P' and Pl2 == 'R'):
        print("Player 1 won!")
    else:
        print("Player 2 won!")
    
if __name__ == "__main__":
    main()