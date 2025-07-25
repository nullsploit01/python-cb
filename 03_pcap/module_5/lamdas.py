def add(a, b):
    return a + b

def square(x):
    return x ** 2

add_lamda = lambda a, b: a + b
print(add_lamda(3, 5))

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

even_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(even_numbers)

# use map with lambda to convert a list of temperature from celcius to fahrenheit (°C * 1.8) + 32
# use filter with lambda to remove all negative numbers from a list