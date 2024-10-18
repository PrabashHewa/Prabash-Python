def main():
    age = int(input("Please, enter your age: "))

    if 17 < age < 25:
        ticket_price =1.47
    elif 7 < age < 17:
        ticket_price =1.02
    elif 0 < age < 7:
        ticket_price =0.00
    else:
        ticket_price =2.04

    print("Your ride will cost:",ticket_price)


if __name__ == "__main__":
    main()