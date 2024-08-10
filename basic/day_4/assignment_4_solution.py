number = input("Enter a number: ")

sum_of_digits = 0

for digit in number:
    sum_of_digits += int(digit)

print(f"{sum_of_digits=}")