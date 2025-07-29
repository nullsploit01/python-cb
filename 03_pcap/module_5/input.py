# name = input("Enter your name: ")
# print("Hello " + name)

# number = int(input("Enter a number: "))
# print(number)

# length = int(input("Enter the length of array: "))

# numbers = []
# for i in range(length):
#     input_number = int(input("Enter number to add in array: "))
#     numbers.append(input_number)
    
# print(numbers)

# numbers = [input("number: ") for i in range(length)]
# print(numbers)

numbers = [int(x) for x in input("Enter numbers: ").split()]
print(numbers)

# print square of all the input numbers using list comprehension
# print only even numbers from input numbers using list comprehension