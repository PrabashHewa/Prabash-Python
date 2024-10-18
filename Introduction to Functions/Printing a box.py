"""
COMP.CS.100 Programming 1
Template for task: box printing
"""

def print_box(w, h, m):
    """
    Print a box with the given width, height, and mark.

    Parameters:
    w : The width of the box.
    h : The height of the box.
    m : The character used to print the box.
    """
    for _ in range(h):
        print(m * w)


def main():
    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
