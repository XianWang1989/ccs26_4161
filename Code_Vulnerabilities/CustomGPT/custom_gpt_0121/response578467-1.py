
# Define your custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Custom function to get the index
def custom_ord(char):
    if char in alphabet:
        return alphabet.index(char)
    else:
        raise ValueError(f"Character '{char}' not in the custom alphabet.")

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
