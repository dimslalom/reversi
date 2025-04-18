# DO NOT modify or add any import statements
from support import *

# Name: Dimas Gistha Adnyana
# Student Number: 49549236
# Favorite Marsupial: Koala
# -----------------------------------------------------------------------------

# Define your functions here (start with def num_hours() -> float)
# Task 1
def num_hours() -> float:
    return 6.4
# Task 2
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
# Task 3
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
# Task 4
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
# Task 5
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
# Task 6
def get_intermediate_locations(position: tuple[int, int], new_position: tuple[int, int]) -> list[tuple[int, int]]:
    """
    Returns a list of (row, column) indexes that lie directly on the line between two indexes (excluding the given indexes). 
    The returned list should be empty if the two indexes do not have a horizontal, vertical, or diagonal line between them.

    Preconditions:

    piece == X or piece == O 
    """
    row_diff = new_position[0] - position[0]
    col_diff = new_position[1] - position[1]
    step_row = 1 if row_diff > 0 else -1
    step_col = 1 if col_diff > 0 else -1
    if abs(row_diff) == abs(col_diff):
        intermediate_locations = [(position[0] + i * step_row, position[1] + i * step_col) for i in range(1, abs(row_diff))]
    elif row_diff == 0:
        intermediate_locations = [(position[0], position[1] + i * step_col) for i in range(1, abs(col_diff))]
    elif col_diff == 0:
        intermediate_locations = [(position[0] + i * step_row, position[1]) for i in range(1, abs(row_diff))]
    else:
        intermediate_locations = []

    return intermediate_locations
# Task 7
def display_board(board: list[list[str]]) -> None:
    """
    Displays the board in a readable format.
    """
    alphabet = "ABCDEFGH"
    print("  12345678")
    print("  --------")
    for i, row in enumerate(board):
        level = f"{alphabet[i]}|"
        for piece in row:
            level += piece
        level += "|"
        print(level)
    print("  --------")
# Task 8
def get_valid_command(valid_moves: list[str]) -> str:
    """
    Returns the first valid command entered by the user.
    valid_moves contains the moves that the current user may make on the board. 
    A move should not be returned if it is not in this list (the Q and H commands are not moves).
    """
    input_command = ""
    while input_command not in valid_moves:
        input_command = input("Please enter move (Or H for help): ")
        if input_command in valid_moves:
            return input_command
# Task 9
def get_reversed_positions(board: list[list[str]], piece: str, position: tuple[int, int]) -> list[tuple[int, int]]:
    """
    Returns every position that would be reversed if the specified piece were placed at the specified position.
    """
    reversed_positions = []

    for row_index, column in enumerate(board):
        for column_index, cell in enumerate(column):
            if cell == piece:
                print(f"Checking cell {chr(column_index + 65)}{row_index + 1} for reversals")
                reversed_positions.extend(get_intermediate_locations(position, (row_index, column_index)))

    return reversed_positions
def check_valid_cell(board: list[list[str]],player: str, position: tuple[int, int]) -> bool:
        player += "+"
        row_index = position[0]
        column_index = position[1]
        if row_index != 0 and row_index != len(board) - 1 and column_index != 0 and column_index != len(board) - 1:
            if (board[row_index + 1][column_index] not in player
            or board[row_index + 1][column_index + 1] not in player
            or board[row_index + 1][column_index - 1] not in player
            or board[row_index - 1][column_index] not in player
            or board[row_index - 1][column_index + 1] not in player
            or board[row_index - 1][column_index - 1] not in player
            or board[row_index][column_index + 1] not in player
            or board[row_index][column_index - 1] not in player):
                return True
        elif row_index == 0 and column_index == 0:
            if (board[row_index + 1][column_index] not in player
            or board[row_index + 1][column_index + 1] not in player
            or board[row_index][column_index + 1] not in player):
                return True
        elif row_index == 0 and column_index == len(board) - 1:
            if (board[row_index + 1][column_index] not in player
            or board[row_index + 1][column_index - 1] not in player
            or board[row_index][column_index - 1] not in player):
                return True
        elif row_index == len(board) - 1 and column_index == 0:
            if (board[row_index - 1][column_index] not in player
            or board[row_index - 1][column_index + 1] not in player
            or board[row_index][column_index + 1] not in player):
                return True
        else:
            return False
# Task 10
def get_available_moves(board: list[list[str]], player: str) -> list[str]:
    """
    Returns the list of available valid moves that the given player can make in the given game state.
    """
    available_moves = []

    for row_index, row in enumerate(board):
        for column_index, cell in enumerate(row):
            if (cell == "+" and check_valid_cell(board, player, (row_index, column_index))):
                position = (row_index, column_index)
                print(f"{chr(column_index + 65)}{row_index + 1}")
                reversed_positions = get_reversed_positions(board, player, position)
                if reversed_positions:
                    move = f"{chr(column_index + 65)}{row_index + 1}"
                    print(f"Adding move: {move}")
                    available_moves.append(move)
    return available_moves



def main() -> None:
    """
    The main function (You should write a better docstring!)
    """
    # print(num_hours())
    # print(move_to_index("A1"))
    # print(generate_empty_board(2))
    # print(generate_initial_board())
    # print(check_winner([["X","X"],["O","X"]]))
    # print(get_intermediate_locations((0,0), (0,3)))
    # print(display_board(generate_initial_board()))
    # get_valid_command(["A1","B4"])
    # board = [["+","+","+","+","+"], ["+","O","O","O","+"], ["+","X","+","X","+"] ,["+","X","X","X","+"], ["+","+","+","+","+"]]
    # display_board(board)
    # print(get_reversed_positions(board, "O", (3,0)))

    board = generate_initial_board()
    display_board(board)
    print(get_available_moves(board, "X"))
    # print(get_intermediate_locations((3,4), (5,2)))
    # print(get_reversed_positions(board, "X", (5,2)))






if __name__ == "__main__":
    main()