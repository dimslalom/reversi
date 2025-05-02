# DO NOT modify or add any import statements
from support import *

# Name: Dimas Gistha Adnyana
# Student Number: 49549236
# Favorite Marsupial: Baby Kangoroo
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
        'H': 7,
        'I': 8,
        'J': 9,
        'K': 10,
        'L': 11,
        'M': 12,
        'N': 13,
        'O': 14,
        'P': 15,
        'Q': 16,
        'R': 17,
        'S': 18,
        'T': 19,
        'U': 20,
        'V': 21,
        'W': 22,
        'X': 23,
        'Y': 24,
        'Z': 25,
    }
    row = letter_to_index[move[0].upper()]
    column = int(move[1: ]) - 1

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
    # Create a list of empty rows
    for x in range(size):
        row = []
        # Create a row with empty cells
        for y in range(size):
            row.append("+")
        empty_board.append(row)
    return empty_board
# Task 4
def generate_initial_board() -> list[list[str]]:
    """
    Generates a board with the initial game state with 8 rows and 8 columns.
    The center 4 squares are filled with the initial pieces of the game.

    >>> generate_initial_board()
    [['+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', 'O', 'X', '+', '+', '+'], ['+', '+', '+', 'X', 'O', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+']]
    
    """
    # Define the size of the board
    initial_board = generate_empty_board(BOARD_SIZE)
    # Place the initial pieces in the center of the board
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
    # Count the number of X and O pieces on the board
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "X":
                x_count += 1
            elif board[row][col] == "O":
                o_count += 1
    # Determine the winner based on the counts
    if x_count > o_count:
        return "X"
    elif o_count > x_count:
        return "O"
    # If both players have the same number of pieces, there is no winner yet
    else:
        return ""
# Task 6
def get_intermediate_locations(position: tuple[int, int], new_position: tuple[int, int]) -> list[tuple[int, int]]:
    """
    Returns a list of (row, column) indexes that lie directly on the line between two indexes (excluding the given indexes). 
    The returned list should be empty if the two indexes do not have a horizontal, vertical, or diagonal line between them.

    Preconditions:

    piece == X or piece == O 

    >>> get_intermediate_locations((0, 0), (0, 3))
    [(0, 1), (0, 2)]
    >>> get_intermediate_locations((5, 0), (1, 0))
    [(4, 0), (3, 0), (2, 0)]
    >>> get_intermediate_locations((1, 1), (4, 4))
    [(2, 2), (3, 3)]
    >>> get_intermediate_locations((0, 0), (1, 2))
    []
    >>> get_intermediate_locations((2, 2), (2, 2))
    []
    >>> get_intermediate_locations((1, 1), (2, 2))
    []
    """
    # Check if the two positions are on the same row, column, or diagonal
    row_diff = new_position[0] - position[0]
    col_diff = new_position[1] - position[1]
    # Determine the direction of movement for each step (1 for positive change, -1 for negative)
    step_row = 1 if row_diff > 0 else -1
    step_col = 1 if col_diff > 0 else -1

    # Check if the movement is diagonal (absolute change in rows equals absolute change in columns)
    if abs(row_diff) == abs(col_diff):
        intermediate_locations = [(position[0] + i * step_row, position[1] + i * step_col) for i in range(1, abs(row_diff))]
    # Check if the movement is horizontal (absolute change in columns only)
    elif row_diff == 0:
        intermediate_locations = [(position[0], position[1] + i * step_col) for i in range(1, abs(col_diff))]
    # Check if the movement is vertical (absolute change in rows only)
    elif col_diff == 0:
        intermediate_locations = [(position[0] + i * step_row, position[1]) for i in range(1, abs(row_diff))]
    # If the movement is neither horizontal, vertical, nor diagonal, return an empty list
    else:
        intermediate_locations = []

    return intermediate_locations
# Task 7
def display_board(board: list[list[str]]) -> None:
    """
    Displays the board in a readable format.
    
    >>> board = [['+', 'X', '+'], ['O', '+', 'X']]
    >>> display_board(board1)
      123
      ---
    A|+X+|
    B|O+X|
      ---
    """
    top_bar = ""
    border = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Check if the board is not empty to avoid index errors
    if not board or not board[0]:
        print("(Empty Board)")
        return
    # Create the top bar and border
    for i in range(len(board[0])):
        top_bar += str(i + 1)
        border += "-" 
    print(f"  {top_bar}\n  {border}")
    # Create the board display
    for i, row in enumerate(board):
        level = f"{alphabet[i]}|"
        # Append each piece/cell content from the current row to the row string
        for piece in row:
            level += piece
        # Add the right border to the row string
        level += "|"
        print(level)
    # Print the bottom border with indentation
    print(f"  {border}")
# Task 8
def get_valid_command(valid_moves: list[str]) -> str:
    """
    Returns the first valid command entered by the user.
    valid_moves contains the moves that the current user may make on the board. 
    A move should not be returned if it is not in this list (the Q and H commands are not moves).
    """
    input_command = ""
    while input_command not in valid_moves:
        input_command = input(MOVE_PROMPT)
        if input_command.upper() == "H":
            return "H"
        elif input_command.upper() == "Q":
            return "Q"
        if input_command.upper() in valid_moves:
            return input_command.upper()
# Task 9
def get_reversed_positions(board: list[list[str]], piece: str, position: tuple[int, int]) -> list[tuple[int, int]]:
    """
    Returns every position that would be reversed if the specified piece were placed at the specified position.
    """
    reversed_positions = []
    # Determine opponent piece
    if piece == 'X':    
        opponent = 'O'
    elif piece == 'O':
        opponent = 'X'
    
    # Store directions to check
    directions = [
        (-1, -1),   (-1, 0),    (-1, 1),
        (0, -1),                (0, 1),
        (1, 1),     (1, 0),     (1, -1)
    ]

    for dr, dc in directions:
        row_index, column_index = (position[0] + dr), (position[1] + dc)
        while 0 <= row_index < len(board) and 0 <= column_index < len(board[0]):
            if board[row_index][column_index] == opponent:
                # Found an opponent piece, continue searching in this direction
                row_index += dr
                column_index += dc
            elif board[row_index][column_index] == piece:
                # Found a piece of the same type, add all positions in between to reversed_positions
                intermediate_locations = get_intermediate_locations(position, (row_index, column_index))
                reversed_positions.extend(intermediate_locations)
                break
            else:
                # Found an empty cell or a piece of the same type, stop searching in this direction
                break
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
    
    >>> get_available_moves([["O", "X", "+", "+", "+", "+", "+", "+"], ["O", "X", "+", "+", "+", "+", "+", "+"], ["O", "O", "X", "X", "X", "X", "O", "+"], ["O", "O", "X", "O", "O", "O", "O", "+"], ["O", "O", "X", "O", "O", "O", "O", "+"], ["O", "O", "X", "O", "O", "O", "O", "+"], ["O"]])
    ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"]
    """
    available_moves = []
    for row_index, row in enumerate(board):
        for column_index, cell in enumerate(row):
            if (cell == "+"):
                position = (row_index, column_index)
                reversed_positions = get_reversed_positions(board, player, position)
                if reversed_positions:
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
    It should display the initial board, and then repeatedly ask the user for a move until the game is over, or the user quits.

    >>> play_game()
    Welcome to Reversi!
      12345678
      --------
    A|++++++++|
    B|++++++++|
    C|++++++++|
    D|+++OX+++|
    E|+++XO+++|
    F|++++++++|
    G|++++++++|
    H|++++++++|
      --------
    Player 1 to move
    Possible moves: C5,D6,E3,F4
    Please enter move (Or H for help): 
    """
    board = generate_initial_board()
    # Count if both players have no moves
    no_moves_counter = 0

    # Initialize the board with the initial game state
    print(WELCOME_MESSAGE)
    player_num = 1
    player_tuple = (PLAYER_1, PLAYER_2)
    player = player_tuple[player_num - 1]

    valid_moves = get_available_moves(board, player)
    # Game loop
    while True:
        valid_moves = get_available_moves(board, player)
        # If valid moves are available for the current player
        if valid_moves:
            while True:
                display_board(board)
                print(f"Player {player_num} to move")
                print("Possible moves: " + ",".join(valid_moves))
                no_moves_counter = 0
                move = get_valid_command(valid_moves)
                if move == "Q":
                # Check for winner
                    winner = check_winner(board)
                    if winner == PLAYER_1:
                        print("Player 1 Wins!")
                    elif winner == PLAYER_2:
                        print("Player 2 Wins!")
                    else:
                        print(DRAW_TEXT)
                    return
                elif move == "H":
                    print(HELP_MESSAGE)
                    continue
                # If the move is valid, make the move
                else:
                    make_move(board, player, move)
                    break
        # If no valid moves are available for the current player
        else:
            display_board(board)
            print(f"Player {player_num} to move")
            print(f"Player {player_num} has no possible move!")    
            no_moves_counter += 1
            # Check if both players have no moves
            if no_moves_counter == 2:
                break
        if player == PLAYER_2:
            player_num = 1
        else:
            player_num = 2
        player = player_tuple[player_num - 1]
    # Check for winner
    winner = check_winner(board)
    if winner == PLAYER_1:
        print("Player 1 Wins!")
    elif winner == PLAYER_2:
        print("Player 2 Wins!")
    else:
        print(DRAW_TEXT)
    return

def main() -> None:
    """
    The main function of the program.
    """
    while True:
        play_game()
        while True:
            play_again = input(PLAY_AGAIN_PROMPT).upper()
            if play_again == "Y" or play_again == "N":
                break
        if play_again != "Y":
            break


    

    






if __name__ == "__main__":
    main()