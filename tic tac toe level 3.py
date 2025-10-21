import random
from rich.console import Console
from rich.text import Text

console = Console()
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
        if i < 2:
            console.print("  --+---+--", justify="center")

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def Intelligence_level(board, computer_choice, player_choice,Difficulty_level,n):

    winning_lines = [
        [0,1,2], [3,4,5], [6,7,8],   
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]             
    ]
    flat_board = [cell for row in board for cell in row]
    if  Difficulty_level =="easy":
            computer = random.choice(n)
            console.print(f"Computer Choice: [cyan]{computer}[/]")
            return computer-1
    elif Difficulty_level =="medium":
        for row in winning_lines:
            value = [flat_board[i] for i in row]
            if value.count(computer_choice) == 2 and value.count(" ") == 1:
                return row[value.index(" ")]
            elif value.count(player_choice) == 2 and value.count(" ") == 1:
                return row[value.index(" ")]
        empty_cells = [i for i, cell in enumerate(flat_board) if cell == " "]
        return random.choice(empty_cells)
    else:
        for row in winning_lines:
            value = [flat_board[i] for i in row]
            if value.count(computer_choice) == 2 and value.count(" ") == 1:
                return row[value.index(" ")]
            if value.count(player_choice) == 2 and value.count(" ") == 1:
                return row[value.index(" ")]
        if flat_board[4]==" ":
            return 4
        for corner in [0, 2, 6, 8]:
            if flat_board[corner] == " ":
                return corner
        empty_cells = [i for i, cell in enumerate(flat_board) if cell == " "]
        return random.choice(empty_cells)

def play(board, number_choice, symbol):
    row, col = divmod(number_choice, 3)  
    board[row][col] = symbol


def play_game(computer_choice, player_choice, Difficulty_level):
    # Initialize empty 3x3 board
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    n = [1,2,3,4,5,6,7,8,9] 
    display_board(board)

    while n:  
        try:
            player = int(input("Enter Num (1-9): ").strip())
        except ValueError:
            console.print("[red]Invalid input — enter a number 1-9[/]")
            continue

        if player not in n:
            console.print("[red]Error Index or already taken, please try again[/]")
            continue

        play(board, player-1, player_choice)  
        n.remove(player)  
        display_board(board)

        check = check_winner(board)
        if check:
            if check == player_choice:
                console.print("\n[green bold]You Are The Winner!\n[/]", justify="center")
                return
            elif check == computer_choice:
                console.print("\n[red bold]You Lost!\n[/]", justify="center")
                return

        if not n:  
            console.print("\n[yellow bold]It's a draw! No winner this time.[/]", justify="center")
            return

        index = Intelligence_level(board, computer_choice, player_choice,Difficulty_level,n) 
        console.print(f"Computer Choice: [cyan]{index+1}[/]")
        play(board, index, computer_choice)
        n.remove(index+1)
        display_board(board)

        check = check_winner(board)
        if check:
            if check == player_choice:
                console.print("\n[green bold]You Are The Winner!\n[/]", justify="center")
                return
            elif check == computer_choice:
                console.print("\n[red bold]You Lost!\n[/]", justify="center")
                return

        if not n:  
            console.print("\n[yellow bold]It's a draw! No winner this time.[/]", justify="center")
            return


console.print("HELLO IN [red bold] X [/] [green bold] O [/] GAME.", justify="center")


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

while True:
    Difficulty_level = input("What difficulty level do you want? (Easy, Medium, Hard): ").strip().lower()
    if Difficulty_level in ["easy","medium", "hard"]:
        break
    console.print("[red bold] Please Enter Choice Only From (Easy, Medium, Hard) [/]")

play_game(computer_choice, player_choice, Difficulty_level)
