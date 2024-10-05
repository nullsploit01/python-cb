# [1, 2, 3, 4, 5] -> TRUE
# [1, 2, 3, 5, 4] -> FALSE
#  0, 1, 2, 3, 4
array = [1, 2, 3, 4, 5]
is_descending = False

# i -> 1
# array[i] = 2
# array[i + 1] -> array[2] = 3
# is 2 > 3? is_sorted = True

is_sorted = True

for i in range(0, len(array) - 1):
    if is_descending:
        if array[i] < array[i + 1]:
            is_sorted = False
    else:
        if array[i] > array[i + 1]:
            is_sorted = False

print(f"{is_sorted=}")