def ia(board, signe):
    """
    Fonction d'IA pour le Tic Tac Toe utilisant l'algorithme minimax
    """

    def check_winner(board):
        """
        Fonction pour vérifier s'il y a un gagnant
        """
        # Vérifier les lignes horizontales
        for i in range(0, 9, 3):
            if board[i] == board[i + 1] == board[i + 2] != 0:
                return board[i]
        # Vérifier les lignes verticales
        for i in range(3):
            if board[i] == board[i + 3] == board[i + 6] != 0:
                return board[i]
        # Vérifier les diagonales
        if board[0] == board[4] == board[8] != 0:
            return board[0]
        if board[2] == board[4] == board[6] != 0:
            return board[2]
        return 0

    def minimax(board, depth, player):
        """
        Fonction principale de l'algorithme minimax
        """
        winner = check_winner(board)
        if winner != 0:
            if winner == signe:
                return 1
            else:
                return -1
        if depth == 9:
            return 0

        if player == signe:
            best = -1
            for i in range(9):
                if board[i] == 0:
                    board[i] = player
                    score = minimax(board, depth + 1, 2 if player == 1 else 1)
                    board[i] = 0
                    best = max(best, score)
            return best
        else:
            best = 1
            for i in range(9):
                if board[i] == 0:
                    board[i] = player
                    score = minimax(board, depth + 1, 2 if player == 1 else 1)
                    board[i] = 0
                    best = min(best, score)
            return best

    best_score = -1
    best_move = -1
    for i in range(9):
        if board[i] == 0:
            board[i] = signe
            score = minimax(board, 0, 2 if signe == 1 else 1)
            board[i] = 0
            if score > best_score:
                best_score = score
                best_move = i
    if best_move == -1:
        return False
    else:
        return best_move
