def create_board():
    board = [[' ' for _ in range(7)] for _ in range(6)]
    return board

def check_win(board, player):
    for row in range(6):
        for col in range(4):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                return True
    for row in range(3):
        for col in range(7):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True
    if board[0][3] == player and board[1][4] == player and board[2][5] == player and board[3][6] == player:
        return True
    if board[3][3] == player and board[2][4] == player and board[1][5] == player and board[0][6] == player:
        return True
    return False

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 21)

def main():
    board = create_board()
    current_player = 'X'
    while True:
        print_board(board)
        col = int(input(f"Player {current_player}, enter a column to drop your piece (1-7): ")) - 1
        if col >= 0 and col < 7 and board[0][col] == ' ':
            for row in range(5, -1, -1):
                if board[row][col] == ' ':
                    board[row][col] = current_player
                    if check_win(board, current_player):
                        print_board(board)
                        print(f"Player {current_player} wins!")
                        break
                    if ' ' not in [cell for row in board for cell in row]:
                        print_board(board)
                        print("It's a draw!")
                    break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid input. Try again.")

if __name__ == '__main__':
    main()