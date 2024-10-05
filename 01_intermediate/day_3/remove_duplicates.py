# Take numbers from user
# Add in array
# Remove duplicate elements 
# Print Array

count_of_numbers = int(input("Enter the count of numbers: "))
array_of_numbers = []

for i in range(0, count_of_numbers):
    input_number  = int(input("Enter a number to add in array: "))
    array_of_numbers.append(input_number)


# [1, 2, 3, 4, 1, 2, 3] -> [1, 2, 3, 4]

filtered_array = []

for number in array_of_numbers:
    if number in filtered_array:
        continue

    filtered_array.append(number)

print(f"Original array: {array_of_numbers}")
print(f"Filtered array: {filtered_array}")