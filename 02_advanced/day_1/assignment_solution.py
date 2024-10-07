import random

def read_high_scores():
    high_scores = {}
    try:
        with open("high_scores.txt", "r") as file:
            for line in file:
                if ":" in line:
                    username, score = line.strip().split(":")
                    high_scores[username] = int(score)
    except FileNotFoundError:
        pass  
    return high_scores

def write_high_scores(high_scores):
    with open("high_scores.txt", "w") as file:
        for username, score in high_scores.items():
            file.write(f"{username}:{score}\n")

def display_menu():
    print("\nWelcome to the Guessing Game!")
    print("1. View High Score")
    print("2. View Leaderboards")
    print("3. Play Game")
    print("4. Exit")
    choice = input("Please enter your choice (1-4): ")
    return choice

def view_high_score(username, high_scores):
    score = high_scores.get(username, "No score recorded.")
    print(f"{username}, your high score is: {score}")

def view_leaderboards(high_scores):
    if high_scores:
        sorted_scores = sorted(high_scores.items())
        print("Leaderboards:")
        for name, score in sorted_scores:
            print(f"{name}: {score}")
    else:
        print("No scores recorded yet.")

def play_game(username, high_scores):
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5
    print("Guess a number between 1 and 100. You have 5 attempts.")

    while attempts < max_attempts:
        guess = input("Enter your guess: ")
        if guess.isdigit():
            guess = int(guess)
            attempts += 1

            if guess == number:
                print("Congratulations! You guessed the correct number!")
                if username in high_scores:
                    if attempts < high_scores[username]:
                        high_scores[username] = attempts
                else:
                    high_scores[username] = attempts
                write_high_scores(high_scores)
                break

            else:
                if guess > number:
                    difference = guess - number
                else:
                    difference = number - guess
                
                if difference < 5:
                    print("Really close!")
                elif difference < 10:
                    print("Close!")
                elif difference < 25:
                    print("A little high!")
                elif difference < 40:
                    print("A little too high!")
                else:
                    print("Too high!")
        else:
            print("Please enter a valid number.")
        
        if attempts == max_attempts:
            print("Game Over! The correct number was", number)

high_scores = read_high_scores()
while True:
    choice = display_menu()
    if choice == "1":
        username = input("Enter your username: ")
        view_high_score(username, high_scores)
    elif choice == "2":
        view_leaderboards(high_scores)
    elif choice == "3":
        username = input("Enter your username to play: ")
        play_game(username, high_scores)
    elif choice == "4":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
