# PALINDROME -> strings that are equal in normal and reversed form
# SOS -> SOS: PALINDROME
# RED -> DER: NOT PALINDROME

user_string = input("enter a string: ").lower()

def reverse_string(string):
    reversed_string = ""

    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]

    return reversed_string

is_palindrome = user_string == reverse_string(user_string)
print(f"{is_palindrome=}")