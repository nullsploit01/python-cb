array = [2, 3, 4, 5, 6, 7, 8, 9,0]

# print 0 if even else 1

modified_array = [0 if x % 2 == 0 else 1 for x in array]

# modified_array = list(map(lambda x: 0 if x % 2 == 0 else 1, array))

print(modified_array)