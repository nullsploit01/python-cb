# Create a 2D list of 4 * 4, take input from user
# Print a list with sum of elements of list in every row of 2d list
# [[1, 2, 3, 4,], [1, 1, 1, 1,], [2, 2, 2, 2,], [3, 3, 3, 3,]] -> [10, 4, 8, 12]

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

list_with_sums = []

for i in range(len(two_d_list)):
    curr_sum = 0
    for j in range(len(two_d_list[i])):
        curr_sum += two_d_list[i][j]

    list_with_sums.append(curr_sum)

print(f"{list_with_sums=}")
