board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

def print_board():
    print("  0 1 2")
    for i in range(3):
        print(i, end=' ')
        for j in range(3):
            print(board[i][j], end=' ')
        print()

def play(player, x, y):
    if board[x][y] != ' ':
        print("Case déjà remplie! Rejouez.")
        return
    board[x][y] = player

def check_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def check_full():
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

player = 'X'
while True:
    print_board()
    x = int(input("Joueur " + player + ", choisissez la ligne (0, 1, 2) : "))
    y = int(input("Joueur " + player + ", choisissez la colonne (0, 1, 2) : "))
    play(player, x, y)
    winner = check_win()
    if winner:
        print("Le gagnant est : " + winner)
        break
    if check_full():
        print("Match nul!")
        break
    if player == 'X':
        player = 'O'
    else:
        player = 'X'