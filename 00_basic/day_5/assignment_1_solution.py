def get_computer_move(user_move, level):
    if level == "1":
        # User always wins
        if user_move == "ROCK":
            return "SCISSORS"
        elif user_move == "PAPER":
            return "ROCK"
        else:  # user_move == "SCISSORS"
            return "PAPER"

    elif level == "2":
        # Computer always wins
        if user_move == "ROCK":
            return "PAPER"
        elif user_move == "PAPER":
            return "SCISSORS"
        else:  # user_move == "SCISSORS"
            return "ROCK"
        
def print_result(user_move, computer_move):
    print(f"Computer's Move: {computer_move}")
    
    if user_move == computer_move:
        print(f"Both players selected {user_move}. It's a tie!")

    elif (user_move == "ROCK" and computer_move == "SCISSORS") or (user_move == "PAPER" and computer_move == "ROCK") or (user_move == "SCISSORS" and computer_move == "PAPER"):
        print(f"{user_move} beats {computer_move}. You win!")

    else:
        print(f"{computer_move} beats {user_move}. You lose.")

user_name = input("Enter Your Name: ")

print("""
    Level 1 - Easy
    Level 2 - Hard
""")

level = input(f"Hello {user_name}! Select Your Level (1 OR 2): ")

if level not in ["1", "2"]:
    print("Invalid Level")
else:
    print("""Choose one of the following:
            - ROCK
            - PAPER
            - SCISSORS
        """)

    user_move = input("Enter your move: ").upper()

    if user_move not in ["ROCK", "PAPER", "SCISSORS"]:
        print("Invalid Move")
    else:
        computer_move = get_computer_move(user_move, level)
        print_result(user_move, computer_move)