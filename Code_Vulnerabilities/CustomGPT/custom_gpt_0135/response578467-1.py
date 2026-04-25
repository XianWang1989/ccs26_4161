
def custom_ord(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"
    # Use index to find the position of the character
    return alphabet.index(char)

# Example usage:
print(custom_ord("a"))  # Outputs: 0
print(custom_ord("b"))  # Outputs: 1
print(custom_ord("c"))  # Outputs: 2
