# Battleship Game
"""
Author: Prabash Madusanka
Description: This program implements a single player version of the Battleship game, where the player
tries to sink the computer's fleet by guessing the locations of the ships.
"""

class Ship:
    def __init__(self, ship_type, coordinates):
        """
        Initialize a Ship object.

        Parameters:
        ship_type : The type of the ship.
        coordinates : List of coordinates occupied by the ship.
        """
        self.ship_type = ship_type
        self.coordinates = [coord.upper() for coord in coordinates]
        self.hits = set()

    def is_hit(self, shot):
        """
        Check if the ship is hit by a shot.

        Parameters:
        shot : The coordinate of the shot.

        Returns:True if the ship is hit, False otherwise.
        """
        if shot in self.coordinates:
            self.hits.add(shot)
            return True
        return False

    def is_sunk(self):
        """
        Check if the ship is sunk.

        Returns: True if the ship is sunk, False otherwise.
        """
        return set(self.coordinates) == self.hits

class Game:
    def __init__(self):
        """
        Initialize a Game object.
        """
        self.ships = []
        self.board = [[' ' for _ in range(10)] for _ in range(10)]
        self.shots = set()

    def read_input_file(self, filename):
        """
        Read the input file and initialize ships.

        Parameters:
        filename : The name of the input file.

        Returns:True if the file is read successfully, False otherwise.
        """
        try:
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(';')
                    ship_type = parts[0]
                    coordinates = parts[1:]
                    if not self.valid_coordinates(coordinates):
                        print("Error in ship coordinates!")
                        return False
                    if self.overlapping_ships(coordinates):
                        print("There are overlapping ships in the input file!")
                        return False
                    self.ships.append(Ship(ship_type, coordinates))
            return True
        except IOError:
            print("File can not be read!")
            return False

    def valid_coordinates(self, coordinates):
        """
        Validate the coordinates.

        Parameters:
        coordinates : List of coordinates to validate.

        Returns:True if all coordinates are valid, False otherwise.
        """
        valid_letters = set("ABCDEFGHIJ")
        valid_digits = set("0123456789")
        for coord in coordinates:
            coord = coord.upper()
            if len(coord) != 2 or coord[0] not in valid_letters or coord[1] not in valid_digits:
                return False
        return True

    def overlapping_ships(self, coordinates):
        """
        Check for overlapping ships.

        Parameters:
        coordinates : List of coordinates to check.

        Returns:True if there are overlapping ships, False otherwise.
        """
        all_coords = set()
        for ship in self.ships:
            all_coords.update(ship.coordinates)
        return any(coord in all_coords for coord in coordinates)

    def display_board(self):
        """
        Display the current state of the game board.
        """
        print()
        header = '  ' + ' '.join("ABCDEFGHIJ")
        print(header)
        for i in range(10):
            row = f"{i} " + ' '.join(self.board[i]) + f" {i}"
            print(row)
        print(header)

    def take_shot(self, shot):
        """
        Process a shot and update the game state.

        Parameters:
        shot : The coordinate of the shot.
        """
        shot = shot.upper()
        if len(shot) != 2 or shot[0] not in "ABCDEFGHIJ" or shot[1] not in "0123456789":
            print("Invalid command!")
            return

        if shot in self.shots:
            print("Location has already been shot at!")
            return

        self.shots.add(shot)
        x, y = ord(shot[0]) - ord('A'), int(shot[1])

        hit_ship = None
        for ship in self.ships:
            if ship.is_hit(shot):
                self.board[y][x] = 'X'
                hit_ship = ship
                break
        else:
            self.board[y][x] = '*'

        if hit_ship and hit_ship.is_sunk():
            print(f"You sank a {hit_ship.ship_type}!")
            for coord in hit_ship.coordinates:
                cx, cy = ord(coord[0]) - ord('A'), int(coord[1])
                self.board[cy][cx] = hit_ship.ship_type[0].upper()

    def all_ships_sunk(self):
        """
        Check if all ships have been sunk.

        Returns:True if all ships are sunk, False otherwise.
        """
        return all(ship.is_sunk() for ship in self.ships)

    def play(self):
        """
        Start the game and handle user input.
        """
        filename = input("Enter file name: ")
        if not self.read_input_file(filename):
            return

        self.display_board()

        while True:
            print()
            shot = input("Enter place to shoot (q to quit): ")
            if shot.lower() == 'q':
                print("Aborting game!")
                break
            self.take_shot(shot)
            self.display_board()
            if self.all_ships_sunk():
                print()
                print("Congratulations! You sank all enemy ships.")
                break

def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()



