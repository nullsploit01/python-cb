def is_list_sorted(array):
    return sorted(array) == array

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

for list in two_d_list:
    print(f"Is {list} sorted? {is_list_sorted(list)}")