# 13 -> 13 % 2 == 0, 13 % 3 == 0, 13 % 4 == 0, ... 13 % 12 == 0

number = int(input("Enter a number: "))

is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False

print(f"{is_prime}")

