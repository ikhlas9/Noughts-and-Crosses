import random
import time

# Initialize the game board
def init_board():
    return [" " for _ in range(9)]

# Print the game board
def print_board(board):
    print("-------------")
    for i in range(3):
        print(f"| {board[3*i]} | {board[3*i + 1]} | {board[3*i + 2]} |")
        print("-------------")
    print("\n\n")

# Print position guide for players
def print_position_guide():
    print("Position guide:")
    print("-------------")
    print("| 1 | 2 | 3 |")
    print("-------------")
    print("| 4 | 5 | 6 |")
    print("-------------")
    print("| 7 | 8 | 9 |")
    print("-------------\n\n")

# Check for a win
def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_combinations)

# Check for a draw
def check_draw(board):
    return all(cell != " " for cell in board)

# Player move
def player_move(board):
    while True:
        try:
            move = int(input("Choose your position (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("That position is already taken. Try again!")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

# Computer move
def computer_move(board):
    print("Computer is thinking...")
    time.sleep(1)  # Pause so its clear on the screen
    while True:
        move = random.randint(0, 8)
        if board[move] == " ":
            board[move] = "O"
            print(f"Computer placed an 'O' at position {move + 1}.\n")
            break

# Main game 
def play_game():
    board = init_board()
    print("Welcome to Noughts and Crosses!\n")
    print_position_guide()
    print_board(board)

    while True:
        # Player's turn
        print("Your turn:")
        player_move(board)
        print_board(board)

        if check_win(board, "X"):
            print("🎉 Congratulations! You win!\n")
            break
        if check_draw(board):
            print("It's a draw!\n")
            break

        # Computer's turn
        print("Computer's turn:")
        computer_move(board)
        print_board(board)

        if check_win(board, "O"):
            print("Computer wins! Better luck next time.\n")
            break
        if check_draw(board):
            print("It's a draw!\n")
            break

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again in ("yes", "y"):
        play_game()
    else:
        print("Thanks for playing! Goodbye 👋")

# Start the game
if __name__ == "__main__":
    play_game()
