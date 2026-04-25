
# Define your custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    # Find the index of the character in the custom alphabet
    index = alphabet.find(char)

    # Check if the character is in the alphabet
    if index == -1:
        raise ValueError(f"Character '{char}' not found in the custom alphabet.")

    return index

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 26
