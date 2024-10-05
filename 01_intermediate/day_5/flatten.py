# Create a 2D list (4 * 4), take input from user
# Flatten it, and store it in an array
# [[1, 2, 3, 4], [1, 1, 1, 1,], [1, 2, 3, 4], [1, 1, 1, 1]] -> [1, 2, 3, 4, 1, 1, 1, 1, 1, 2 ,3, 4, 1, 1, 1, 1]

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

print(f"{two_d_list=}")
flattened_list = []

for i in range(len(two_d_list)):
    for j in range(len(two_d_list[i])):
        flattened_list.append(two_d_list[i][j])


print(f"{flattened_list=}")