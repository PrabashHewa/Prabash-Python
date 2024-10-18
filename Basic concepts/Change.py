def main():
    
    Pl1 = int(input("Purchase price: "))
    Pl2 = int(input("Paid amount of money: "))
    
    change = Pl2 - Pl1
    if change <=0 :
        print("No change")
    else:
        print("Offer change:")
        
        tense = change//10 
        if tense > 0:
            print(f"{tense} ten-euro notes")
            
        fives = (change % 10) // 5
        if fives > 0:
            print(f"{fives} five-euro notes")
            
        twose =((change % 10) % 5) // 2
        if twose > 0:
            print(f"{twose} two-euro coins")
            
        once = (((change % 10) % 5) % 2) // 1
        if once > 0 :
            print(f"{once} one-euro coins")
    
if __name__ == "__main__":
    main()