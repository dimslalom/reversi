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
    row = letter_to_index[move[0].upper()]
    column = int(move[1]) - 1

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
    top_bar = ""
    border = ""
    alphabet = "ABCDEFGH"
    for i in range(len(board[0])):
        top_bar += str(i + 1)
        border += "-" 
    print(f"  {top_bar}\n  {border}")
    for i, row in enumerate(board):
        level = f"{alphabet[i]}|"
        for piece in row:
            level += piece
        level += "|"
        print(level)
    print(f"  {border}")
# Task 8
def get_valid_command(valid_moves: list[str]) -> str:
    """
    Returns the first valid command entered by the user.
    valid_moves contains the moves that the current user may make on the board. 
    A move should not be returned if it is not in this list (the Q and H commands are not moves).
    """
    input_command = ""
    valid_moves.extend(["Q", "H"])
    while input_command not in valid_moves:
        input_command = input("Please enter move (Or H for help): ")
        if input_command.upper() in valid_moves:
            print(input_command)
            return input_command.upper()
# Task 9
def get_reversed_positions(board: list[list[str]], piece: str, position: tuple[int, int]) -> list[tuple[int, int]]:
    """
    Returns every position that would be reversed if the specified piece were placed at the specified position.
    """
    reversed_positions = []

    for row_index, column in enumerate(board):
        for column_index, cell in enumerate(column):
            if cell == piece:
                reversed_positions.extend(get_intermediate_locations(position, (row_index, column_index)))

    return reversed_positions
def check_valid_cell(board: list[list[str]], player: str, row_index: int, column_index: int) -> bool:
    """
    Checks if board[row_index][column_index] is empty and has an adjacent opponent piece.
    """
    board_height = len(board)
    if board_height == 0:
        return False
    board_width = len(board[0])

    # Check if target indices are within board boundaries
    if not (0 <= row_index < board_height and 0 <= column_index < board_width):
        return False

    # Check if the target cell is empty
    if board[row_index][column_index] != "+":
        return False
    

    # Determine opponent
    if player == 'X':
        opponent = 'O'
    elif player == 'O':
        opponent = 'X'
    else:
        return False # Invalid player input

    # Check 8 neighbors for an opponent's piece
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue # Skip the current cell

            neighbor_r, neighbor_c = row_index + dr, column_index + dc

            # Check if neighbor coordinates are within bounds
            if 0 <= neighbor_r < board_height and 0 <= neighbor_c < board_width:
                # Check if this valid neighbor contains the opponent's piece
                if board[neighbor_r][neighbor_c] == opponent:
                    return True # Valid move: empty cell with adjacent opponent

    # If loop finishes, no adjacent opponent was found
    return False
def get_placed_pieces(board: list[list[str]]) -> list[tuple[int, int]]:
    """
    Returns a list of all the pieces that have been placed on the board.
    """
    placed_pieces = []
    for row_index, row in enumerate(board):
        for column_index, cell in enumerate(row):
            if cell != "+":
                placed_pieces.append((row_index, column_index))
    return placed_pieces
# Task 10
def get_available_moves(board: list[list[str]], player: str) -> list[str]:
    """
    Returns the list of available valid moves that the given player can make in the given game state.
    """
    available_moves = []
    placed_pieces = get_placed_pieces(board)

    for row_index, row in enumerate(board):
        for column_index, cell in enumerate(row):
            # print(cell)
            # print(f"{chr(row_index + 65)}{column_index + 1}")
            # print(check_valid_cell(board, player, row_index, column_index))
            if (cell == "+" and check_valid_cell(board, player, row_index, column_index)):
                position = (row_index, column_index)
                reversed_positions = get_reversed_positions(board, player, position)

                # print("Reversed positions: ", reversed_positions)
                # print("Placed pieces: ", placed_pieces)


                # Check if all reversed positions are in placed_pieces
                all_found = True
                for element in reversed_positions:
                    if element not in placed_pieces:
                        all_found = False
                        break

                if reversed_positions and all_found:
                    move = f"{chr(row_index + 65)}{column_index + 1}"
                    available_moves.append(move)
    return available_moves
# Task 11
def make_move(board: list[list[str]], piece: str, move: str) -> None:
    """
    Makes a move on the board by placing the specified piece at the specified position. 
    The function should also reverse all pieces that are between the new piece and any other pieces of the same type.

    Preconditions:
    move is a valid move, given in upper case
    move corresponds to a valid position on the board
    each row of board will contain the same number of columns
    """
    row_index, column_index = move_to_index(move)
    board[row_index][column_index] = piece
    reversed_positions = get_reversed_positions(board, piece, (row_index, column_index))
    for position in reversed_positions:
        board[position[0]][position[1]] = piece
# Task 12
def play_game() -> None:
    """
    The main function of the game. 
    It should display the initial board, and then repeatedly ask the user for a move until the game is over.
    """
    board = generate_initial_board()
    print("Welcome to Reversi!")
    player = "X"
    display_board(board)
    valid_moves = get_available_moves(board, player)
    print("Player 1 to move")
    print("Possible moves: " + ",".join(valid_moves))
    while valid_moves:
        move = get_valid_command(valid_moves)
        print("You entered: " + move)
        if move == "Q":
            return
        elif move == "H":
            print("[A-H][1-8]: Place piece at specified square. \n H/h: Display help message. \n Q/q: Quit current game.")
            continue
        else:
            make_move(board, player, move)
        display_board(board)
        if player == "O":
            player = "X"
            print("Player 1 to move")
        else:
            player = "O"
            print("Player 2 to move")
        valid_moves = get_available_moves(board, player)
        print("Possible moves: " + ",".join(valid_moves))


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
    # board = generate_initial_board()
    # display_board(board)
    # print(get_reversed_positions(board, "O", (3,0)))

    # board = [["+","+","+","+","+"], ["+","O","O","O","+"], ["+","X","+","X","+"] ,["+","X","X","X","+"], ["+","+","+","+","+"]]
    # display_board(board)
    # print(get_available_moves(board, "O"))

    play_game()
    # make_move(board, "X", "D3")
    # display_board(board)

    

    






if __name__ == "__main__":
    main()