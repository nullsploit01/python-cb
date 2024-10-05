count_of_numbers = int(input("Enter the count of numbers: "))
array_of_numbers = []

for i in range(0, count_of_numbers):
    input_number  = int(input("Enter a number to add in array: "))
    array_of_numbers.append(input_number)

number_to_remove = int(input("Enter a number to remove from array: "))

filtered_array = []

for number in array_of_numbers:
    if number == number_to_remove:
        continue

    filtered_array.append(number)

print(f"Array after removing {number_to_remove} -> {filtered_array}")