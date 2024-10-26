ages = [4, 16, 32, 19, 11, 17, 15, 23, 124, 28, 21, 22]

# every age above 18

adults = list(filter(lambda x: x >=18, ages))
print(adults)