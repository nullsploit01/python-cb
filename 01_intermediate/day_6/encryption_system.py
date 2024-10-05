def shift_char(c, shift):
    """Helper function to shift a single character."""
    if ' ' <= c <= '~':  # Shift only printable characters
        return chr((ord(c) - 32 + shift) % 95 + 32)
    return c

def encrypt_level_1(text, shift=3):
    """Encrypts text using a simple Caesar cipher with a specified shift."""
    encrypted_text = ''
    for c in text:
        encrypted_text += shift_char(c, shift)
    return encrypted_text

def decrypt_level_1(text, shift=3):
    """Decrypts text that was encrypted using the above mapping."""
    decrypted_text = ''
    for c in text:
        decrypted_text += shift_char(c, -shift)
    return decrypted_text

def encrypt_level_2(text, cols=5):
    """Columnar transposition encryption with clear padding handling."""
    padding_char = 'X'  # used for padding, unlikely to appear in normal text
    padding = (cols - len(text) % cols) % cols
    text += padding_char * padding  # Append padding using a distinct character
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
    decrypted_text = ''.join(decrypted)
    if padding > 0:
        decrypted_text = decrypted_text[:-padding]  # Remove padding
    return decrypted_text.rstrip('X')  # Also strip any stray padding characters

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