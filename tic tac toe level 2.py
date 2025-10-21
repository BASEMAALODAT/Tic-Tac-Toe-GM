import random
from rich.console import Console
from rich.text import Text

console = Console()

# Function to display the current game board with styled output
def display_board(board):
    for i, row in enumerate(board):
        row_display = []
        for cell in row:
            if cell == "X":
                row_display.append(Text("X", style="red bold"))
            elif cell == "O":
                row_display.append(Text("O", style="green bold"))
            else:
                row_display.append(Text(" "))
        console.print(*row_display, sep=" | ", justify="center")
        if i < 2:  # Add separator between rows
            console.print("  --+---+--", justify="center")

# Function to check if there is a winner
def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None  # No winner yet

# Function for computer decision-making (medium mode AI)
def Intelligence_level(board, computer_choice, player_choice):

    # All possible winning line combinations
    winning_lines = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]
    # Flatten the 2D board into 1D for easier index handling
    flat_board = [cell for row in board for cell in row]

    # Check if computer can win or block the player
    for row in winning_lines:
        value = [flat_board[i] for i in row]
        # If computer can win
        if value.count(computer_choice) == 2 and value.count(" ") == 1:
            return row[value.index(" ")]
        # If player is about to win -> block them
        elif value.count(player_choice) == 2 and value.count(" ") == 1:
            return row[value.index(" ")]
    return None  # No immediate winning/blocking move

# Function to place a move on the board
def play(board, number_choice, symbol):
    """
    The code defines a Tic-Tac-Toe game where the player can choose their symbol and the difficulty
    level to play against the computer.
    
    :param board: The `board` parameter represents the Tic-Tac-Toe game board, which is a 3x3 grid where
    players place their symbols (X or O) during the game. The board is represented as a 2D list in the
    code, where each element corresponds to a cell on the
    :param number_choice: The `number_choice` parameter in the `play` function represents the player's
    choice of position on the Tic-Tac-Toe board. It is an integer value ranging from 1 to 9, where each
    number corresponds to a position on the 3x3 board. The function then converts
    :param symbol: The `symbol` parameter in the `play` function represents the symbol (either "X" or
    "O") that will be placed on the board at the specified position chosen by the player or the computer
    during the game
    """
    row, col = divmod(number_choice, 3)  # Convert index into row, col
    board[row][col] = symbol

# Main game loop
def play_game(computer_choice, player_choice, Difficulty_level):
    # Initialize empty 3x3 board
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    # List of available moves (1-9)
    n = [1,2,3,4,5,6,7,8,9] 
    display_board(board)

    while n:  # Continue until board is full
        # ---- Player Move ----
        try:
            player = int(input("Enter Num (1-9): ").strip())
        except ValueError:
            console.print("[red]Invalid input — enter a number 1-9[/]")
            continue

        if player not in n:
            console.print("[red]Error Index or already taken, please try again[/]")
            continue

        play(board, player-1, player_choice)  # Place player move
        n.remove(player)  # Remove from available moves
        display_board(board)

        # Check winner after player move
        check = check_winner(board)
        if check:
            if check == player_choice:
                console.print("\n[green bold]You Are The Winner!\n[/]", justify="center")
                return
            elif check == computer_choice:
                console.print("\n[red bold]You Lost!\n[/]", justify="center")
                return

        if not n:  # If no moves left -> draw
            console.print("\n[yellow bold]It's a draw! No winner this time.[/]", justify="center")
            return

        # ---- Computer Move ----
        if Difficulty_level == "easy":
            # Computer plays randomly
            computer = random.choice(n)
            console.print(f"Computer Choice: [cyan]{computer}[/]")
            play(board, computer - 1, computer_choice)
            n.remove(computer)

        elif Difficulty_level == "medium":
            # Computer tries to win or block
            index = Intelligence_level(board, computer_choice, player_choice)  
            if index is None:  # No smart move found -> random
                computer = random.choice(n)
                console.print(f"Computer Choice: [cyan]{computer}[/]")
                play(board, computer - 1, computer_choice)
                n.remove(computer)
            else:  # Play smart move
                console.print(f"Computer Choice: [cyan]{index+1}[/]")
                play(board, index, computer_choice)
                n.remove(index+1)

        display_board(board)

        # Check winner after computer move
        check = check_winner(board)
        if check:
            if check == player_choice:
                console.print("\n[green bold]You Are The Winner!\n[/]", justify="center")
                return
            elif check == computer_choice:
                console.print("\n[red bold]You Lost!\n[/]", justify="center")
                return

        if not n:  # If no moves left -> draw
            console.print("\n[yellow bold]It's a draw! No winner this time.[/]", justify="center")
            return


# ---- Game Starts Here ----
console.print("HELLO IN [red bold] X [/] [green bold] O [/] GAME.", justify="center")

# Choose player symbol
while True:
    game = input("""\nIf You Want:
    1. O enter (1 Or O)
    2. X Enter (2 Or X) : """).strip().lower()
    if game in ["o","1"]:
        player_choice = "O"
        computer_choice = "X"
        break
    elif game in ["x","2"]:
        player_choice = "X"
        computer_choice = "O"
        break
    else:
        console.print("\n[red bold] ERROR CHOICE, PLEASE TRY AGAIN[/]")

# Choose difficulty level
while True:
    Difficulty_level = input("What difficulty level do you want? (Easy, Medium): ").strip().lower()
    if Difficulty_level in ["easy","medium"]:
        break
    console.print("[red bold] Please Enter Choice Only From (Easy, Medium) [/]")

# Start the game
play_game(computer_choice, player_choice, Difficulty_level)