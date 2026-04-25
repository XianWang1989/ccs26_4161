
def custom_ord(char, alphabet="abcdefghijklmnopqrstuvwxyz0123456789 .,?!"):
    # Get the index of the character in the custom alphabet
    index = alphabet.find(char)

    # If the character is found, return its index, otherwise return a suitable response (e.g., -1)
    return index if index != -1 else None

# Example usage:
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("z"))  # Output: 25
