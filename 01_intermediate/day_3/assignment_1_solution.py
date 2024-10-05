count_of_numbers = int(input("Enter the count of numbers: "))
array_of_numbers = []

for i in range(0, count_of_numbers):
    input_number  = int(input("Enter a number to add in array: "))
    array_of_numbers.append(input_number)

sum_of_numbers = 0

for number in array_of_numbers:
    sum_of_numbers += number

print(f"{sum_of_numbers=}")