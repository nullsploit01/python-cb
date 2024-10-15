# def get_key(x):
#     return x[0]

# two_d_array = [[5, 1, 7], [2, 3, 8], [4, 6, 9]]
# print(sorted(two_d_array, key = get_key))
# print(sorted(two_d_array, key = lambda x: x[0]))

dict = {"a": 25, "b": 1, "d": 1, "c": 11}
print(sorted(dict.items(), key=lambda x: x[1]))