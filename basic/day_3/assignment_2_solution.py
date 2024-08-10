user_string = input("Enter a string: ")
user_alphabet = input("Enter an alphabet: ")

if user_alphabet == "a" or user_alphabet == "e" or user_alphabet == "i" or user_alphabet == "o" or user_alphabet == "u":
    print("Cannot search for vowels!")

else:
    occurences = 0
    for character in user_string:
        if character == user_alphabet:
            occurences += 1

    print(f"Alphabet '{user_alphabet}' occured {occurences} times in string '{user_string}'")