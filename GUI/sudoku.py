def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(grid, row, col, num):
    # Check if num is not in the current row, column, and 3x3 subgrid
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(grid):
    empty = find_empty_location(grid)
    if not empty:
        return True  # Puzzle solved
    row, col = empty

    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0  # Undo assignment and try again

    return False  # Trigger backtracking

def find_empty_location(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def get_user_input():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    print("Enter the initial numbers with coordinates (e.g., 0 0 5 for row 0, column 0, number 5). Enter 'done' when finished:")
    
    while True:
        user_input = input("Enter coordinate and number: ")
        if user_input.lower() == 'done':
            break
        try:
            row, col, num = map(int, user_input.split())
            if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9:
                grid[row][col] = num
            else:
                print("Invalid input. Please enter values in the range row(0-8), column(0-8), and number(1-9).")
        except ValueError:
            print("Invalid input format. Please enter row, column, and number separated by spaces.")
    
    return grid

def main():
    grid = get_user_input()
    print("Initial Sudoku grid:")
    print_grid(grid)
    
    if solve_sudoku(grid):
        print("Solved Sudoku grid:")
        print_grid(grid)
    else:
        print("No solution exists for the given Sudoku puzzle.")

if __name__ == "__main__":
    main()
