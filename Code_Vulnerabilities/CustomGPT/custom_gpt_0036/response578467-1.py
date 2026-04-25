
def custom_ord(char, alphabet="abcdefghijklmnopqrstuvwxyz0123456789 .,?!"):
    # Find the index of the character in the custom alphabet string
    index = alphabet.find(char)
    # Return the index if found, or -1 if the character is not in the alphabet
    return index if index != -1 else -1  # Return -1 for characters not found

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord(" "))  # Output: 26 (space is at index 26)
print(custom_ord("?"))  # Output: 32 (question mark is at index 32)
print(custom_ord("!"))  # Output: 31 (exclamation mark is at index 31)
print(custom_ord("Z"))  # Output: -1 (since 'Z' is not in the alphabet)
