def longest_word(string):
    current_word = ""
    longest_word = ""

    for char in string + " ":  
        if char != " ":
            current_word += char
        else:
            if len(current_word) > len(longest_word):
                longest_word = current_word
            current_word = ""

    return longest_word

print(longest_word("I LOVE PROGRAMMING")) 
print(longest_word("I HAVE THE BEST BOOK"))  