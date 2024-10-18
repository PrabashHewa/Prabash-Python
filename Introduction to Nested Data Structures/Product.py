"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Template for the product assignment.
"""

class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    def __init__(self, name, price):
        """
        Initialize a product with its name and price.

        :param name: str, the name of the product.
        :param price: float, the price of the product.
        """

        self.__name = name
        self.__price = price
        self.__sale_percentage = 0.0

    def printout(self):
        """
        Print out the details of the product.
        """

        print("=" * 20)
        print(f"{self.__name}")
        print(f"  price: {self.__price:.2f}")
        print(f"  sale%: {self.__sale_percentage:.2f}")

    def set_sale_percentage(self, sale_percentage):
        """
        Set the sale percentage of the product.

        :param sale_percentage: float, the percentage by which to discount the product.
        """

        self.__sale_percentage = sale_percentage

    def get_price(self):
        """
        Get the current sale price of the product.

        :return: float, the current sale price of the product.
        """

        return self.__price * (1 - self.__sale_percentage / 100)


def main():
    test_products = {
        "milk": 1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
