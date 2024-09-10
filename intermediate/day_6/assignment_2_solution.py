squares = {}

for i in range(1, 1001):
    squares[i] = i ** 2

number = int(input("Enter a number from 1 - 1000: "))

if 0 < number > 1000:
    print("invalid number")
else:
    print(f"Square of {number} is {squares[number]}")