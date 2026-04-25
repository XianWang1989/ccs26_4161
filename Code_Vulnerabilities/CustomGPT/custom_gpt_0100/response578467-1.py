
def custom_ord(char, alphabet):
    if char in alphabet:
        return alphabet.index(char)
    return None  # Return None or an error for characters not in the alphabet

# Your custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Test the function
print(custom_ord("a", alphabet))  # Output: 0
print(custom_ord("b", alphabet))  # Output: 1
print(custom_ord("c", alphabet))  # Output: 2
print(custom_ord("1", alphabet))  # Output: 26
print(custom_ord(" ", alphabet))   # Output: 36
