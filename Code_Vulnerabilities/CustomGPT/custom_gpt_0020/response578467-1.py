
# Define the custom alphabet string
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    """Return the index of the char in the custom alphabet, or None if char is not found."""
    index = alphabet.find(char)
    if index == -1:
        raise ValueError(f"Character '{char}' not found in the custom alphabet.")
    return index

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 26
print(custom_ord(" "))  # Output: 36
print(custom_ord("?"))  # Output: 39
