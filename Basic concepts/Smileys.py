def main():
    
    mood = int(input("How do you feel? (1-10) "))
    if mood == 1 :
        print("A suitable smiley would be :'(")
    elif 1< mood < 4:
        print("A suitable smiley would be :-(")
    elif 4 <= mood <= 7:
        print("A suitable smiley would be :-|")
    elif 7 < mood < 10:
        print("A suitable smiley would be :-)")
    elif mood ==10 :
        print("A suitable smiley would be :-D")
    else:
        print("Bad input!")
    
if __name__ == "__main__":
    main()