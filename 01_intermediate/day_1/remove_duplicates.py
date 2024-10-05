# STRING : I LOVE PROGRAMMING -> I LOVE PRGAMN

string = "I LOVE PROGRAMMING"

non_duplicate_string = ""

for character in string:
    if character not in non_duplicate_string or character.isspace():
        non_duplicate_string += character

print(f"{non_duplicate_string=}")