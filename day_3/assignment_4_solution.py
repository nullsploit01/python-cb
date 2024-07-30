number = int(input("Enter a number: "))

sum_of_factors = 0

for i in range(1, 501):
    if number % i == 0:
        sum_of_factors += i

print(f"{sum_of_factors=}")