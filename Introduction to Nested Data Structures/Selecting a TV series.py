"""
COMP.CS.100 Programming 1
Read genres and tv-series from a file into a dict.
Print a list of the genres in alphabetical order
and list tv-series by given genre on user's command.
"""

def read_file(filename):
    """
    Reads and saves the series and their genres from the file.

    :param filename: name of the file to read
    :return: dictionary containing genres as keys and lists of series as values
    """

    genre_data = {}

    try:
        file = open(filename, mode="r")

        for row in file:
            name, genres = row.rstrip().split(";")
            genres = genres.split(",")

            for genre in genres:
                if genre in genre_data:
                    genre_data[genre].append(name)
                else:
                    genre_data[genre] = [name]

        file.close()
        return genre_data

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)

    if genre_data:
        print("Available genres are:", ", ".join(sorted(genre_data.keys())))

        while True:
            genre = input("> ")

            if genre == "exit":
                return

            if genre in genre_data:
                for series in sorted(genre_data[genre]):
                    print(series)

if __name__ == "__main__":
    main()
