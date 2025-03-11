PLAYER = 'X'
AI = 'O'
EMPTY = ' '

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
def check_winner(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def minimax(board, is_maximizing):
    if check_winner(board, AI): return 1
    if check_winner(board, PLAYER): return -1
    if all([board[i][j] != EMPTY for i in range(3) for j in range(3)]): return 0

    best_score = -float('inf') if is_maximizing else float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI if is_maximizing else PLAYER
                score = minimax(board, not is_maximizing)
                board[i][j] = EMPTY
                best_score = max(score, best_score) if is_maximizing else min(score, best_score)
    return best_score

def ai_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                score = minimax(board, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]
    print_board(board)

    while True:
        row, col = map(int, input("Enter your move (row and column 0-2): ").split())
        if board[row][col] == EMPTY:
            board[row][col] = PLAYER
        else:
            print("Invalid move. Try again.")
            continue
        print_board(board)

        if check_winner(board, PLAYER):
            print("You win!")
            break
        if all([board[i][j] != EMPTY for i in range(3) for j in range(3)]):
            print("It's a tie!")
            break

        print("AI's turn:")
        row, col = ai_move(board)
        board[row][col] = AI
        print_board(board)

        if check_winner(board, AI):
            print("AI wins!")
            break

play_game()
