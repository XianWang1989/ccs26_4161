
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    """Returns the position of char in the custom alphabet, starting from 0."""
    return alphabet.index(char)

# Example usage
print(custom_ord("a"))  # Outputs: 0
print(custom_ord("b"))  # Outputs: 1
print(custom_ord("c"))  # Outputs: 2
