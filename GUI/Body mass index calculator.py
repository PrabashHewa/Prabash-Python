"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Body Mass Index template
"""

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        # Label and Entry for weight
        weight_label = Label(self.__mainwindow, text="Weight (kg):")
        weight_label.grid(row=0, column=0, padx=5, pady=5)
        self.__weight_value = Entry(self.__mainwindow)
        self.__weight_value.grid(row=0, column=1, padx=5, pady=5)

        # Label and Entry for height
        height_label = Label(self.__mainwindow, text="Height (cm):")
        height_label.grid(row=1, column=0, padx=5, pady=5)
        self.__height_value = Entry(self.__mainwindow)
        self.__height_value.grid(row=1, column=1, padx=5, pady=5)

        # Button for calculating BMI
        self.__calculate_button = Button(self.__mainwindow, text="Calculate BMI", command=self.calculate_BMI)
        self.__calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Label for displaying BMI result
        self.__result_text = Label(self.__mainwindow, text="")
        self.__result_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # Label for displaying verbal description of BMI
        self.__explanation_text = Label(self.__mainwindow, text="")
        self.__explanation_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Button for stopping the program
        self.__stop_button = Button(self.__mainwindow, text="Stop", command=self.stop)
        self.__stop_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def calculate_BMI(self):
        """
        Calculates the BMI based on the entered weight and height values.
        """
        # Clear previous error messages
        self.__explanation_text["text"] = ""

        # Clear previous BMI result
        self.__result_text["text"] = ""

        # Get the weight and height entered by the user
        weight_str = self.__weight_value.get()
        height_str = self.__height_value.get()

        # Check if weight and height are numbers
        try:
            weight = float(weight_str)
            height = float(height_str)
        except ValueError:
            self.__explanation_text["text"] = "Error: height and weight must be numbers."
            self.reset_fields()
            return

        # Check if weight and height are positive
        if weight <= 0 or height <= 0:
            self.__explanation_text["text"] = "Error: height and weight must be positive."
            self.reset_fields()
            return

        # Convert height from cm to meters
        height /= 100

        # Calculate BMI using the formula: weight / height^2
        bmi = weight / (height ** 2)

        # Display the calculated BMI with two decimal places
        self.__result_text["text"] = f"{bmi:.2f}"

        # Display verbal explanation of BMI
        if 18.5 <= bmi <= 25:
            self.__explanation_text["text"] = "Your weight is normal."
        elif bmi > 25:
            self.__explanation_text["text"] = "You are overweight."
        else:
            self.__explanation_text["text"] = "You are underweight."

    def reset_fields(self):
        """
        Resets the contents of the elements __result_text, __height_value and __weight_value.
        """
        self.__result_text["text"] = ""
        self.__height_value.delete(0, 'end')
        self.__weight_value.delete(0, 'end')

    def stop(self):
        """
        Ends the execution of the program.
        """
        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately. Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
