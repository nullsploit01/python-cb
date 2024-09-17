# take a array of input from user
# remove duplicate values
# [1, 2, 3, 2, 5, 2] -> [1, 2, 3, 5]

array = [1, 2, 3, 2, 5, 2]
# filtered_array = []

# for num in array:
#     if num in filtered_array:
#         continue
#     filtered_array.append(num)

# print(f"{filtered_array=}")

filtered_array = list(set(array))
print(f"{filtered_array=}")