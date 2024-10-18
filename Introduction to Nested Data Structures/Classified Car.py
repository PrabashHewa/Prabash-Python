"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Code template for a simplified car assignment
implementation using a class.
"""

class Car:
    """
    Class Car: Implements a car that moves a certain distance and
    whose gas tank can be filled. The class defines what a car is:
    what information it contains and what operations can be
    carried out for it.
    """

    def __init__(self, tank_size, gas_consumption):
        """
        Constructor, initializes the newly created object.

        :param tank_size: float, the size of this car's tank.
        :param gas_consumption: float, how much gas this car consumes
                   when it drives a 100 kilometers
        """

        self.__tank_volume = tank_size
        self.__consumption = gas_consumption
        self.__gas = 0.0  # initializing gas attribute
        self.__odometer = 0.0  # initializing odometer attribute

    def print_information(self):
        """
        Method to print the current information about the car:
        the amount of gas in the tank and the odometer reading.
        """

        print(f"The tank contains {self.__gas:.1f} liters of gas "
              f"and the odometer shows {self.__odometer:.1f} kilometers.")

    def fill(self, amount):
        """
        Method to fill the car's gas tank with the given amount of gas.

        :param amount: float, amount of gas to fill in liters.
        """

        if amount < 0:
            print("You cannot remove gas from the tank")
        else:
            self.__gas = min(self.__tank_volume, self.__gas + amount)

    def drive(self, distance):
        """
        Method to drive the car for a given distance.

        :param distance: float, distance to drive in kilometers.
        """

        if distance < 0:
            print("You cannot travel a negative distance")
        else:
            # Calculate gas consumption for the given distance
            gas_needed = (self.__consumption / 100) * distance

            # Check if there is enough gas to cover the distance
            if gas_needed <= self.__gas:
                self.__gas -= gas_needed
                self.__odometer += distance
            else:
                # If there is not enough gas, drive until the tank is empty
                self.__odometer += (self.__gas * 100) / self.__consumption
                self.__gas = 0


def main():
    tank_size = read_number("How much does the vehicle's gas tank hold?")
    gas_consumption = read_number("How many liters of gas does the car "
                                  "consume per hundred kilometers?")

    car = Car(tank_size, gas_consumption)

    while True:
        car.print_information()

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up?")
            car.fill(to_fill)

        elif choice == "2":
            distance = read_number("How many kilometers to drive?")
            car.drive(distance)

        elif choice == "3":
            print("Thank you and bye!")
            break


def read_number(prompt, error_message="Incorrect input!"):
    """
    This function is used to read input (float) from the user.

    :param prompt: str, prompt to be used when asking user input.
    :param error_message: str, what error message to print
        if the entered value is not a float.
    """

    while True:
        try:
            return float(input(prompt + " "))

        except ValueError:
            print(error_message)


if __name__ == "__main__":
    main()
