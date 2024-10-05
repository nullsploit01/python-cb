def flatten_2d_list(list_to_flatten):
    curr_flattened_list = []
    for i in range(len(list_to_flatten)):
        for j in range(len(list_to_flatten[i])):
            curr_flattened_list.append(list_to_flatten[i][j])

    return curr_flattened_list

rows = 4
cols = 4

two_d_list = []

for i in range(0, cols):
    curr_list = []

    for j in range(0, rows):
        curr_num = int(input("Enter a number: "))
        curr_list.append(curr_num)

    two_d_list.append(curr_list)
    print(f"{curr_list} added to 2D list")

sorted_two_d_list = []
sorted_flattened_2d_list = sorted(flatten_2d_list(two_d_list))

curr_iterator = 0
for i in range(0, cols):
    curr_list = []

    for j in range(0, rows):
        curr_list.append(sorted_flattened_2d_list[curr_iterator])
        curr_iterator += 1
    sorted_two_d_list.append(curr_list)

print(f"{sorted_two_d_list=}")