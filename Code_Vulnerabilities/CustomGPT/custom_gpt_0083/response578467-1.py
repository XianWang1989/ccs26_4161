
# Define your custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    # Get the index of the character in the custom alphabet
    index = alphabet.find(char)
    return index if index != -1 else None  # Return None if char is not found

# Example usage
print(custom_ord('a'))  # Output: 0
print(custom_ord('b'))  # Output: 1
print(custom_ord('c'))  # Output: 2
