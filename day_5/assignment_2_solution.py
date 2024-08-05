user_name = input("Enter Your Name: ")
user_choice = 0

def greet(name):
    print(f"Hello {name}!")

def get_factorial(number):
    factorial = 1

    for i in range(1, number + 1):
        factorial = factorial * i

    return factorial

def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def factorial(a):
    return get_factorial(a)

def square(a):
    return a ** 2

def cube(a):
    return a ** 3

greet(user_name)

while True:
    print("""
        What operation would you like to perform? 
        1 -> Addition
        2 -> Substraction
        3 -> Multiplication
        4 -> Division
        5 -> Factorial
        6 -> Square
        7 -> Cube
        8 -> Close Calculator
    """)

    user_choice = int(input("Select one from above: "))

    if user_choice == 8:
        print("Closing Calculator. Goodbye!")
        break

    if user_choice == 1:
        number_one = float(input("Enter first number: "))
        number_two = float(input("Enter second number: "))
        print(f"The result of {number_one} + {number_two} is: {addition(number_one, number_two)}")

    elif user_choice == 2:
        number_one = float(input("Enter first number: "))
        number_two = float(input("Enter second number: "))
        print(f"The result of {number_one} - {number_two} is: {substraction(number_one, number_two)}")

    elif user_choice == 3:
        number_one = float(input("Enter first number: "))
        number_two = float(input("Enter second number: "))
        print(f"The result of {number_one} * {number_two} is: {multiplication(number_one, number_two)}")

    elif user_choice == 4:
        number_one = float(input("Enter first number: "))
        number_two = float(input("Enter second number: "))
        if number_two != 0:
            print(f"The result of {number_one} / {number_two} is: {division(number_one, number_two)}")
        else:
            print("Division by zero is not allowed.")

    elif user_choice == 5:
        number = int(input("Enter a number: "))
        print(f"The factorial of {number} is: {factorial(number)}")

    elif user_choice == 6:
        number = int(input("Enter a number: "))
        print(f"The square of {number} is: {square(number)}")

    elif user_choice == 7:
        number = int(input("Enter a number: "))
        print(f"The cube of {number} is: {cube(number)}")

    else:
        print("Invalid selection. Please choose a valid option.")
