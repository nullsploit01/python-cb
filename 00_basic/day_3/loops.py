# break, continue

print_even = True

for i in range(1, 21):
    if print_even and i % 2 != 0:
        continue

    if not print_even and i % 2 == 0:
        continue

    print(i)

    