count_of_numbers = int(input("Enter the count of numbers to add: "))
array_of_numbers = []

for i in range(0, count_of_numbers):
    input_number  = int(input("Enter a number to add in array of numbers: "))
    array_of_numbers.append(input_number)

count_of_numbers_to_remove = int(input("Enter the count of numbers to remove: "))
array_of_numbers_to_remove = []

for i in range(0, count_of_numbers_to_remove):
    input_number  = int(input("Enter a number to add in array of numbers to remove: "))
    array_of_numbers_to_remove.append(input_number)

filtered_array = []

for number in array_of_numbers:
    if number in array_of_numbers_to_remove:
        continue

    filtered_array.append(number)

print(f"Filtered array, after removing {array_of_numbers_to_remove} from {array_of_numbers} -> {filtered_array}")