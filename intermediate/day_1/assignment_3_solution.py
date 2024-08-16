def remove_char(string, char_to_remove):
    result = ""
    for char in string:
        if char != char_to_remove:
            result += char
    return result

print(remove_char("THIS IS A STRING, S", "S"))  
print(remove_char("THIS IS A RED DRESS, R", "R"))  