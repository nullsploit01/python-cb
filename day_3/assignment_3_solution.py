sum_of_even_numbers = 0
sum_of_odd_numbers = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum_of_odd_numbers += i

    else:
        sum_of_even_numbers += i

print(f"{sum_of_even_numbers=}, {sum_of_odd_numbers=}")