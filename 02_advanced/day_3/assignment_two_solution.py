add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else 'Division by zero error'
cube = lambda x: x ** 3
square = lambda x: x ** 2

def calculator():
    print("Options:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Cube\n6. Square")
    choice = int(input("Choose your operation (1-6): "))

    if choice in [1, 2, 3, 4]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operations = {1: add, 2: subtract, 3: multiply, 4: divide}
        result = operations[choice](num1, num2)
        print(f"Result: {result}")

    elif choice in [5, 6]:
        num = float(input("Enter the number: "))
        operations = {5: cube, 6: square}
        result = operations[choice](num)
        print(f"Result: {result}")

    else:
        print("Invalid choice")

calculator()