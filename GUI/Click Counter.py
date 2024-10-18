"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 0123456
Name:       Xxxx Yyyyyy
Email:      xxxx.yyyyyy@tuni.fi

Code template for counter program.
"""

from tkinter import *

class Counter:
    def __init__(self):
        self.__counter_value = 0
        
        # Create the Tkinter window
        self.__window = Tk()
        self.__window.title("Counter Program")
        
        # Create and place the label to display the counter value
        self.__current_value_label = Label(self.__window, text=str(self.__counter_value))
        self.__current_value_label.pack()
        
        # Create the buttons
        self.__reset_button = Button(self.__window, text="Reset", command=self.reset_counter)
        self.__reset_button.pack()
        
        self.__increase_button = Button(self.__window, text="Increase", command=self.increase_counter)
        self.__increase_button.pack()
        
        self.__decrease_button = Button(self.__window, text="Decrease", command=self.decrease_counter)
        self.__decrease_button.pack()
        
        self.__quit_button = Button(self.__window, text="Quit", command=self.__window.quit)
        self.__quit_button.pack()

        # Run the Tkinter event loop
        self.__window.mainloop()
    
    def reset_counter(self):
        self.__counter_value = 0
        self.__current_value_label.config(text=str(self.__counter_value))
        
    def increase_counter(self):
        self.__counter_value += 1
        self.__current_value_label.config(text=str(self.__counter_value))
        
    def decrease_counter(self):
        self.__counter_value -= 1
        self.__current_value_label.config(text=str(self.__counter_value))


def main():
    Counter()

if __name__ == "__main__":
    main()
