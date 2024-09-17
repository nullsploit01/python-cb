# two arrays, 
# [1, 2, 3, 4, 5], [4, 5, 6, 7, 8]
# print the common elements of two arrays
# [4, 5]

array_one = [1, 2, 3, 4, 5]
array_two = [4, 5, 6, 7, 8]

set_of_array_one = set(array_one)
set_of_array_two = set(array_two)

intersection = set_of_array_one.intersection(set_of_array_two)
print(f"{intersection=}")