string = "I like to play football"
alphabet = "i"

# count number of alphabet in string

count_of_alphabets = 0

for x in string:
    if x == alphabet:
        count_of_alphabets += 1

print(count_of_alphabets)