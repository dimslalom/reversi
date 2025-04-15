# DO NOT modify or add any import statements
from support import *

# Name: Dimas Gistha Adnyana
# Student Number: 49549236
# Favorite Marsupial: Koala
# -----------------------------------------------------------------------------

# Define your functions here (start with def num_hours() -> float)
def num_hours() -> float:
    return 6.4

def move_to_index(move: str) -> tuple[int, int]:
    """
    Returns the (row, column) index on the board corresponding to a player’s move. 
    The first row on the board is the topmost one, and the first column on the board is the leftmost one. 
    The returned index should begin at 0, that is the top left corner should have index (0,0).

    >>> move_to_index("A1")
    (0, 0)
    >>> move_to_index("H8")
    (7, 7)
    """
    letter_to_index = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7
    }
    column = letter_to_index[move[0].upper()]
    row = int(move[1]) - 1

    return (row, column)

def generate_empty_board(size: int) -> list[list[str]]:
    """
    Generates an empty board with a specified number of rows. 
    The generated board will be square (The number of columns will equal the number of rows). 
    Empty board positions are marked with +

    Preconditions:
    size >= 0

    >>> generate_empty_board(1)
    [['+']]
    >>> generate_empty_board(2)
    [['+', '+'], ['+', '+']]
     """
    empty_board = []
    for x in range(size):
        row = []
        for y in range(size):
            row.append("+")
        empty_board.append(row)
    return empty_board

def generate_initial_board() -> list[list[str]]:
    """
    Generates a board with the initial game state with 8 rows and 8 columns.
    The center 4 squares are filled with the initial pieces of the game.
    """
    initial_board = generate_empty_board(8)
    initial_board[3][3] = "O"
    initial_board[3][4] = "X"
    initial_board[4][3] = "X"
    initial_board[4][4] = "O"
    return initial_board

def check_winner(board: list[list[str]]) -> str:
    """
    Checks the board for a winner. 
    The function should return "X" if player X has won, "O" if player O has won, and "" if there is no winner yet.

    Preconditions:
    board is a valid game board

    >>> check_winner([["X", "O", "+", "+", "+", "+", "+", "+"], ["O", "X", "+", "+", "+", "+", "+", "+"], ["O", "O", "X", "X", "X", "X", "O", "+"], ["O", "O", "X", "O", "O", "O", "O", "+"], ["O", "O", "X", "O", "O", "O", "O", "+"], ["O", "O", "X", "O", "O", "O", "O", "+"], ["O", "O", "X", "O", "O", "O", "O", "+"], ["+", "+", "+", "+", "+", "+", "+", "+"]])
    "X"
    """
    x_count = 0
    o_count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "X":
                x_count += 1
            elif board[row][col] == "O":
                o_count += 1
    if x_count > o_count:
        return "X"
    elif o_count > x_count:
        return "O"
    else:
        return ""
    
def get_intermediate_locations(position: tuple[int, int], new_position: tuple[int, int]) -> list[tuple[int, int]]:
    """
    Returns a list of (row, column) indexes that lie directly on the line between two indexes (excluding the given indexes). 
    The returned list should be empty if the two indexes do not have a horizontal, vertical, or diagonal line between them.

    Preconditions:

    piece == X or piece == O 
    """
    

def main() -> None:
    """
    The main function (You should write a better docstring!)
    """
    print(num_hours())
    print(move_to_index("A1"))
    # print(generate_empty_board(2))
    # print(generate_initial_board())
    print(check_winner([["X","X"],["O","X"]]))


if __name__ == "__main__":
    main()