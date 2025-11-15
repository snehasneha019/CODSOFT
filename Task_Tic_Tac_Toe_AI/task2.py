

def print_board(board):
    print()
    for i in range(3):
        row = board[i*3 : i*3+3]
        print(row[0], "|", row[1], "|", row[2])
        if i < 2:
            print("---------")
    print()

def check_winner(board):
    
    wins = [
        [0,1,2], [3,4,5], [6,7,8],   
        [0,3,6], [1,4,7], [2,5,8],   
        [0,4,8], [2,4,6]             
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "Draw"
    return None

def minimax(board, is_max):
    winner = check_winner(board)
    if winner == "X":
        return 1
    if winner == "O":
        return -1
    if winner == "Draw":
        return 0

    if is_max:
        best_score = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

def get_ai_move(board):
    best_score = -100
    best_move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def play_game():
    board = [" "] * 9
    print("Tic Tac Toe - You (O) vs Computer (X)")
    print_board(board)

    while True:
        
        move = int(input("Enter position (1-9): ")) - 1
        if board[move] != " ":
            print("Spot taken, try again.")
            continue
        board[move] = "O"
        print_board(board)

        if check_winner(board):
            print("Result:", check_winner(board))
            break

        
        print("Computer thinking...")
        ai_move = get_ai_move(board)
        board[ai_move] = "X"
        print_board(board)

        if check_winner(board):
            print("Result:", check_winner(board))
            break


play_game()
