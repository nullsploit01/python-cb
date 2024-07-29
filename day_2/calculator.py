name = input("What is your name? = ")
print(f"Hello {name}!")

number_one = int(input("Enter first number: "))
number_two = int(input("Enter second number: "))

print("""
    What operation would you like to perform? 
    1 -> Addition
    2 -> Substraction
    3 -> Multiplication
""")

operation = input("Select one from above: ")

if operation == "1":
    print(f"Addition of these two numbers is: {number_one + number_two}")

elif operation == "2":
    print(f"Substraction of these two numbers is: {number_one - number_two}")

elif operation == "3":
    print(f"Multiplication of these two numbers is: {number_one * number_two}")

else:
    print("Incorrect Choice!")

