def is_list_sorted(array):
    return sorted(array) == array

def flatten_2d_list(list_to_flatten):
    curr_flattened_list = []
    for i in range(len(list_to_flatten)):
        for j in range(len(list_to_flatten[i])):
            curr_flattened_list.append(list_to_flatten[i][j])

    return curr_flattened_list


cols = 3
rows = 4

two_d_list = []

for i in range(0, cols):
    curr_list = []

    for j in range(0, rows):
        curr_num = int(input("Enter a number: "))
        curr_list.append(curr_num)

    two_d_list.append(curr_list)
    print(f"{curr_list} added to 2D list")


flattened_list = flatten_2d_list(two_d_list)

print(f"{flattened_list=}")
print(f"Is {flattened_list} Sorted? {is_list_sorted(flattened_list)}")