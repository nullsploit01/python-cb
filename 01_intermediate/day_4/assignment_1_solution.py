count_of_numbers = int(input("Enter the count of numbers: "))
array_of_numbers = []

for i in range(0, count_of_numbers):
    input_number  = int(input("Enter a number to add in array: "))
    array_of_numbers.append(input_number)

print(f"{array_of_numbers=}")

number_to_remove = int(input("Enter number to remove: "))

for i in range(len(array_of_numbers)):
    if array_of_numbers[i] == number_to_remove:
        array_of_numbers[i] = 0

print(f"{array_of_numbers=}")


