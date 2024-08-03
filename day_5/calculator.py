# Make an infinite calculator
# Take input from user, and perform operaions like addition, substraction, multiplication, division

user_name = input("Enter Your Name: ")
user_choice = 0

def greet(name):
    print(f"Hello {name}!")

def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b



while True:
    print("""
        What operation would you like to perform? 
        1 -> Addition
        2 -> Substraction
        3 -> Multiplication
        4 -> Division
        5 -> Close Calculator
    """)

    user_choice = int(input("Select one from above: "))

    if user_choice == 5:
        break

    number_one = int(input("Enter first number: "))
    number_two = int(input("Enter second number: "))
    
    if user_choice == 1:
        print(f"Addition of two numbers: {addition(number_one, number_two)}")

    if user_choice == 2:
        print(f"Substraction of two numbers: {substraction(number_one, number_two)}")

    if user_choice == 3:
        print(f"Multiplication of two numbers: {multiplication(number_one, number_two)}")

    if user_choice == 4:
        print(f"Division of tow numbers: {division(number_one, number_two)}")

    

    

    



