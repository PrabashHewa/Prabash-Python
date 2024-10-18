"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id:
Name:
Email:

Template for pricelist assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}

def main():
    while True:
        product_name = input("Enter product name: ").strip()
        
        if not product_name:  
            print("Bye!")
            break
        
        product_name = product_name.lower()  
        
        if product_name in PRICES:  
            price = PRICES[product_name]
            print(f"The price of {product_name} is {price:.2f} e")
        else:
            print(f"Error: {product_name} is unknown.")

if __name__ == "__main__":
    main()

