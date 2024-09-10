def encrypt_level_1(text, shift=3):
    """Applies a Caesar cipher with a specified shift to all characters."""
    return ''.join(chr((ord(char) - 32 + shift) % 95 + 32) if ' ' <= char <= '~' else char for char in text)

def decrypt_level_1(text, shift=3):
    """Reverses the Caesar cipher applied in Level 1."""
    return ''.join(chr((ord(char) - 32 - shift) % 95 + 32) if ' ' <= char <= '~' else char for char in text)

def encrypt_level_2(text, cols=5):
    """Uses a columnar transposition method with a specified number of columns."""
    # Ensure the text fills the matrix by adding necessary padding.
    padding = (cols - len(text) % cols) % cols
    text += ' ' * padding
    # Create the encrypted text by reading columns of the matrix.
    encrypted = ''
    for col in range(cols):
        for index in range(col, len(text), cols):
            encrypted += text[index]
    return encrypted, padding

def decrypt_level_2(encrypted, cols, padding):
    """Reverses the columnar transposition of Level 2."""
    rows = len(encrypted) // cols
    decrypted = [''] * rows
    for col in range(cols):
        for row in range(rows):
            index = col * rows + row
            if index < len(encrypted):
                decrypted[row] += encrypted[index]
    # Join the rows into a single string and remove the padding.
    return ''.join(decrypted).rstrip()[:-padding] if padding else ''.join(decrypted).rstrip()

def encrypt_level_3(text):
    """Reverses the text."""
    return text[::-1]

def decrypt_level_3(text):
    """Reverses the text to return to original state."""
    return text[::-1]

def encrypt_level_4(text):
    """Swaps the case of each letter in the text."""
    return text.swapcase()

def decrypt_level_4(text):
    """Reverses the case swapping to return to the original text."""
    return text.swapcase()

def main():
    user_text = input("Enter some text to encrypt: ")
    print("Original text:", user_text)
    
    encrypted1 = encrypt_level_1(user_text)
    print("After Level 1 Encryption:", encrypted1)
    
    encrypted2, padding = encrypt_level_2(encrypted1)
    print("After Level 2 Encryption:", encrypted2)
    
    encrypted3 = encrypt_level_3(encrypted2)
    print("After Level 3 Encryption:", encrypted3)
    
    encrypted4 = encrypt_level_4(encrypted3)
    print("Fully Encrypted text:", encrypted4)
    
    decrypted4 = decrypt_level_4(encrypted4)
    print("After reversing Level 4 Encryption:", decrypted4)
    
    decrypted3 = decrypt_level_3(decrypted4)
    print("After reversing Level 3 Encryption:", decrypted3)
    
    decrypted2 = decrypt_level_2(decrypted3, 5, padding)
    print("After reversing Level 2 Encryption:", decrypted2)
    
    decrypted1 = decrypt_level_1(decrypted2)
    print("Decrypted back to original:", decrypted1)

if __name__ == "__main__":
    main()