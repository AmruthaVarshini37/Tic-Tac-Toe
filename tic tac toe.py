import random

board = [' ' for _ in range(9)]

def print_board():
    row1 = f"{board[0]} | {board[1]} | {board[2]}"
    row2 = f"{board[3]} | {board[4]} | {board[5]}"
    row3 = f"{board[6]} | {board[7]} | {board[8]}"
    print(row1)
    print('--+---+--')
    print(row2)
    print('--+---+--')
    print(row3)

def check_winner(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_full():
    return ' ' not in board

def make_move(player, position):
    if board[position] == ' ':
        board[position] = player
        return True
    return False

def ai_move():
    available_moves = [i for i, spot in enumerate(board) if spot == ' ']
    return random.choice(available_moves)

def play_game():
    current_player = 'X' 
    game_on = True
    
    while game_on:
        print_board()
        
        if current_player == 'X':
            move = int(input("Player X, choose your move (1-9): ")) - 1
        else:
            move = ai_move()
            print(f"Player O (AI) chooses move: {move + 1}")
        
        if move < 0 or move >= 9:
            print("Invalid move. Please try again.")
            continue

        if make_move(current_player, move):
            if check_winner(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                game_on = False
            elif check_full():
                print_board()
                print("It's a tie!")
                game_on = False
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That spot is already taken. Please try again.")
if __name__ == "__main__":
    play_game()
