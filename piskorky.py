"""
piskvorky.py: druhý projekt do Engeto Online Python Akademie
author: Tomáš Pernikář
email: tomworld@seznam.cz
discord: Tomáš P.#9699
"""

# Vytvoříme hrací plochu jako list listů
Board = list[list[str]]

def display_board(board: Board) -> None:
    """
    Funkce vytiskne hrací plochu. Každý vnitřní seznam představuje jeden řádek hrací plochy.
    """
    for row in board:
        print("+---+---+---+")
        print("| " + " | ".join(row) + " |")
    print("+---+---+---+")

def tic_tac_toe() -> None:
    """
    Tisk pravidel hry.
    """
    print("Welcome to Tic Tac Toe")
    print("========================================")
    print("GAME RULES:")
    print("Each player can place one mark (or stone) per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("========================================")
    print("Let's start the game")

def check_win(board: Board, player: str) -> bool:
    """
    Funkce ověřuje, zda hráč vyhrál.
    """
    # horizontály
    for row in board:
        if row.count(player) == 3:
            return True
    
    # vertikály
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    
    # diagonály
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    
    return False


def check_tie(board: Board) -> bool:
    """
    Funkce ověřuje, zda nejsou všechna hrací pole obsazena, tedy remízu.
    """
    for row in board:
        if " " in row:
            return False
    return True

# zobrazení pravidel
tic_tac_toe()

# inicializace hrací plochy o velikosti 3X3 
board = [[" " for _ in range(3)] for _ in range(3)]
display_board(board)
    
# hrací smyčka
players = ["X", "O"]
turn = 0

while True:
    # vyber hráče
    player = players[turn % 2]
    
    # vyzvání hráče k volbě pole
    move = input(f"\nPlayer {player} | Please enter your move number: ")
    
    # ověření správnosti vstupu
    if not move.isdigit():
        print("Invalid input! Please enter a number.")
        continue
    
    move = int(move)
    if move < 1 or move > 9:
        print("Invalid input! Please enter a number from 1 to 9.")
        continue
    
    # převod čísla na pozici v hracím poli
    row = (move - 1) // 3
    col = (move - 1) % 3
    
    # kontrola, zda je pole volné
    if board[row][col] != " ":
        print("This field is already taken!")
        continue
    
    # umístění znaku hráče na pole
    board[row][col] = player
    
    # vypsání aktuálního stavu hrací plochy
    display_board(board)

    # kontrola výhry
    if check_win(board, player):
        print(f"Congratulations, the player {player} WON!")
        break

    # kontrola remízy
    if check_tie(board):
        print("The game ended in a tie!")
        break
    # předání tahu druhému hráči
    turn += 1

    