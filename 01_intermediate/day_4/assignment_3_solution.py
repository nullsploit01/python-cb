rows = 3
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

number_to_count = int(input("Enter a number to change: "))
count = 0

for i in range(len(two_d_list)):
    for j in range(len(two_d_list[i])):
        if two_d_list[i][j] == number_to_count:
            count += 1

print(f"{count=}")