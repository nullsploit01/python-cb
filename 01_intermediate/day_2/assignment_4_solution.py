def get_factorial(number):
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    return factorial


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for num in array:
    print(f"factorial of {num} = {get_factorial(num)}")