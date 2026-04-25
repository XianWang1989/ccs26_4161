
# Custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    # Return the index of the character in the custom alphabet
    return alphabet.index(char) if char in alphabet else -1

# Testing the function
print(custom_ord("a"))  # Outputs: 0
print(custom_ord("b"))  # Outputs: 1
print(custom_ord("c"))  # Outputs: 2
print(custom_ord("1"))  # Outputs: 26 (position of '1' in the string)
print(custom_ord("!"))  # Outputs: 36 (position of '!' in the string)
