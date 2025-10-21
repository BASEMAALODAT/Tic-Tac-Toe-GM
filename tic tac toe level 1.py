import random  
from rich.console import Console 
from rich.text import Text 

# Create a Console object to print styled text
console = Console()

# Function to display the Tic Tac Toe board
def display_board(board):
    # Loop through each row of the board with its index (i = 0,1,2)
    for i, row in enumerate(board):
        row_display = []  # Store formatted cells for the current row

        # Check each cell and add styled text depending on its value
        for cell in row:
            if cell == "X":
                row_display.append(Text("X", style="red bold"))   # Red X
            elif cell == "O":
                row_display.append(Text("O", style="green bold")) # Green O
            else:
                row_display.append(Text(" "))  # Empty cell

        # Print the current row, separated by " | " and centered
        console.print(*row_display, sep=" | ", justify="center")

        # Print a divider line below the row (except after the last one)
        if i < 2: 
            console.print("  --+---+--", justify="center")

# Function to check if there is a winner
def check_winner(board):
    # Check rows for a winner
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check columns for a winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

# Function to place a symbol on the board
def play(board, number_choice, symbol):
    row, col = divmod(number_choice, 3)   # Convert 0-8 index to (row, col)
    board[row][col] = symbol

# Main function to handle the game loop
def play_game(computer_choice, player_choice): 
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]  # Initialize empty board
    display_board(board)  # Show empty board at start
    n = [1,2,3,4,5,6,7,8,9]  # Available positions

    while n:  # Continue while there are available positions
        # Player move
        player = int(input("Enter Num (1-9): "))
        if player in n: 
            index = player-1
            play(board, index, player_choice)  # Place player's symbol
            n.remove(player)  # Remove chosen position from available moves
        else:
            print("Error Index, Please Try Again")
            continue  # Ask player again if input invalid

        # Check if player has won
        check = check_winner(board)
        if check:
            if check == "O":
                console.print("\n[green bold]You Are The Winner!\n[/]", justify="center")
                break
            elif check == "X":
                console.print("\n[red bold]You Lost!\n[/]", justify="center")
                break   
        
        # Computer move if positions are left
        if n:  
            computer = random.choice(n)  # Randomly select from available positions
            console.print(f"Computer Choice: [cyan]{computer}[/]")
            index2 = computer - 1
            play(board, index2, computer_choice)  # Place computer's symbol
            n.remove(computer)  # Remove chosen position

        display_board(board)  # Show updated board

        # Check if computer has won
        check = check_winner(board)
        if check:
            if check == "O":
                console.print("\n[green bold]You Are The Winner!\n[/]", justify="center")
                break
            elif check == "X":
                console.print("\n[red bold]You Lost!\n[/]", justify="center")
                break
        # If no moves left and no winner, it's a draw
        elif not n:
            console.print("\n[yellow bold]It's a draw! No winner this time.[/]", justify="center")


# Welcome message and game instructions
console.print("HELLO IN [red bold] X [/] [green bold] O [/] GAME.", justify="center")

# Ask the player which symbol they want to play
game = input("""\nIf You Want:
    1. O enter (1 Or O)
    2. X Enter (2 Or X) : """).lower()

# Validate input and start the game
while True:
    if game not in ["o", "x" , "1" , "2"]:
        console.print("\n[red bold] ERROR CHOICE, PLEASE TRY AGAIN[/]")
        print()
        game = input("""If You Want:
        1. O enter (1 Or O)
        2. X Enter (X Or 2) : """).lower()
    elif game in ["o", "1"]:
        play_game("X", "O")  # Player is O, computer is X
    else:
        play_game("O", "X")  # Player is X, computer is O
