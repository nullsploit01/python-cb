import random

HIGH_SCORE_FILE = "high_score.txt"

def get_high_score():
    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return 0

def set_high_score(score):
    try:
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(score))
    except Exception as e:
        print(f"Error writing high score: {e}")

def play_game():
    user_score = 0
    cpu_score = 0
    rounds = 0

    while rounds < 5:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue
        
        cpu_choice = random.choice(["rock", "paper", "scissors"])
        print(f"CPU chose: {cpu_choice}")
        
        if user_choice == cpu_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and cpu_choice == "scissors") or \
             (user_choice == "paper" and cpu_choice == "rock") or \
             (user_choice == "scissors" and cpu_choice == "paper"):
            print("You win this round!")
            user_score += 1
        else:
            print("CPU wins this round!")
            cpu_score += 1
        
        rounds += 1
        print(f"Score -> You: {user_score}, CPU: {cpu_score}")

    print("\nGame over!")
    if user_score > cpu_score:
        print("Congratulations! You won the game.")
    elif cpu_score > user_score:
        print("CPU wins the game. Better luck next time!")
    else:
        print("The game ended in a tie!")

    high_score = get_high_score()
    if user_score > high_score:
        print(f"New high score! Your score: {user_score}")
        set_high_score(user_score)
    else:
        print(f"Your score: {user_score}. Current high score: {high_score}")

def show_high_score():
    high_score = get_high_score()
    print(f"High Score: {high_score}")

while True:
    print("\n--- Rock Paper Scissors Menu ---")
    print("1. Play Game")
    print("2. Show High Score")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice (1-3): "))
        if choice == 1:
            play_game()
        elif choice == 2:
            show_high_score()
        elif choice == 3:
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    except ValueError:
        print("Invalid input! Please enter a number (1-3).")
    except Exception as e:
        print(f"An error occurred: {e}")
    
