# Take numbers from user
# Add it in array
# Take a number from user, and print its occurences inside that array.

count_of_numbers = int(input("Enter the count of numbers: "))
array_of_numbers = []

for i in range(0, count_of_numbers):
    input_number  = int(input("Enter a number to add in array: "))
    array_of_numbers.append(input_number)

number_to_count = int(input("Enter a number to count occurences: "))
occurences = 0

for number in array_of_numbers:
    if number == number_to_count:
        occurences += 1

print(f"Occurences of {number_to_count} in array: {occurences}")