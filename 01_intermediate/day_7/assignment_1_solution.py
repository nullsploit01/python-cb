string = "this is a string 1 2 3 $#"
frequencies = {}

for alphabet in string:
    if not alphabet.isalpha():
        continue

    if alphabet in frequencies:
        frequencies[alphabet] += 1
    else:
        frequencies[alphabet] = 1

print(frequencies)