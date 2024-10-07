import random
correct_answer = random.randint(1,100)
user_answer = int(input("Enter number guess: "))
if abs(correct_answer-user_answer) <= 5:
    print("really close. ")
if abs(correct_answer-user_answer) <= 10:
    print("close. ")
if abs(correct_answer-user_answer) <= 15:
    print("little far. ")
if abs(correct_answer-user_answer) <= 20:
    print("way far. ")