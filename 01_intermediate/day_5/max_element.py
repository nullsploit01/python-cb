# Create a 2D list (4 * 4), take input from user
# Print MAX element from every row in 2D list
# [[1, 2, 3, 4], [1, 2, 1, 1], [1, 2, 3, 7], [8, 9, 11, 12]] -> 4, 2, 7, 12

def get_max_number(array):
    current_max = array[0]

    for i in array:
        if i > current_max:
            current_max = i

    return current_max

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

for i in range(len(two_d_list)):
    print(get_max_number(two_d_list[i]))



