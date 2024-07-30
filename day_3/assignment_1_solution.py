number_1 = int(input("Enter Number 1: "))
number_2 = int(input("Enter Number 2: "))
number_3 = int(input("Enter Number 3: "))
number_4 = int(input("Enter Number 4: "))

greatest_odd = 0
greatest_even = 0

if number_1 % 2 == 0:
    greatest_even = number_1
else:
    greatest_odd = number_1

if number_2 % 2 == 0:
    if greatest_even == 0 or number_2 > greatest_even:
        greatest_even = number_2
else:
    if greatest_odd == 0 or number_2 > greatest_odd:
        greatest_odd = number_2

if number_3 % 2 == 0:
    if greatest_even == 0 or number_3 > greatest_even:
        greatest_even = number_3
else:
    if greatest_odd == 0 or number_3 > greatest_odd:
        greatest_odd = number_3

if number_4 % 2 == 0:
    if greatest_even == 0 or number_4 > greatest_even:
        greatest_even = number_4
else:
    if greatest_odd == 0 or number_4 > greatest_odd:
        greatest_odd = number_4

print(f"{greatest_even=}, {greatest_odd=}")