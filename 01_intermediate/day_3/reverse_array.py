# Take numbers from user
# Insert it in array
# Reverse that array

count_of_numbers = int(input("Enter the count of numbers: "))
array_of_numbers = []

for i in range(0, count_of_numbers):
    input_number  = int(input("Enter a number to add in array: "))
    array_of_numbers.append(input_number)

print(f"Your array: {array_of_numbers}")
array_of_numbers.reverse()
print(f"Your array Reversed: {array_of_numbers}")
