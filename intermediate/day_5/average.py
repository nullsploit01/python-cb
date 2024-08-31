# Create a 2D list (3 * 4), take inout from user
# Print average of every row in 2d list
# [[1, 2, 3, 4], [1, 1, 1, 1], [2, 2, 2, 2]] -> [2.5, 1, 2]

def get_average(array):
    current_sum = 0

    for i in array:
        current_sum += i

    return current_sum / len(array)

rows = 4
cols = 3

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
    print(get_average(two_d_list[i]))