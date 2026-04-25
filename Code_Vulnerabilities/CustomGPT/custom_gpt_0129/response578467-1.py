
def custom_ord(char, alphabet):
    # Find the index of the character in the alphabet string
    index = alphabet.find(char)
    # Return the index, which maps to 'ord' like behavior
    return index if index != -1 else None

# Define your custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Example usage
print(custom_ord("a", alphabet))  # Output: 0
print(custom_ord("b", alphabet))  # Output: 1
print(custom_ord("c", alphabet))  # Output: 2
print(custom_ord("0", alphabet))  # Output: 26
print(custom_ord(" ", alphabet))  # Output: 36
