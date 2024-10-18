"""
COMP.CS.100 Programming 1
Code template for "replacing grades" program
"""


def convert_grades(grades):
    """ Check if the grades list is empty, if so, return early. Otherwise 
    Loop over the grades list to replace grades greater than zero with 6
    """
    for i in range(len(grades)):
        if grades[i] > 0:
            grades[i] = 6



def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
