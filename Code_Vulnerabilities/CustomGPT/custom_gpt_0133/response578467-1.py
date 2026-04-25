
def custom_ord(char, alphabet):
    # Get the index of the character in the alphabet string
    index = alphabet.find(char)
    if index == -1:
        raise ValueError(f"Character '{char}' not found in the alphabet string.")
    return index

# Define your custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Examples
print(custom_ord("a", alphabet))  # Output: 0
print(custom_ord("b", alphabet))  # Output: 1
print(custom_ord("c", alphabet))  # Output: 2
