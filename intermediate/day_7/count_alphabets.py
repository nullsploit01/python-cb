# strring -> this is a string
# write function to get occurences of every alphabet in that string
# -> t -> 2, h -> 1, i -> 3....

string = 'this is a string'

frequencies = {}

for i in string:
    if i in frequencies:
        frequencies[i] += 1
    else:
        frequencies[i] = 1

print(frequencies)
        