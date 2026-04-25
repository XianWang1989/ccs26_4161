alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Custom function to get "ord" values based on the custom alphabet
def custom_ord(char):
    return alphabet.index(char)

# Example usage
print(custom_ord("a"))  # Outputs: 0
print(custom_ord("b"))  # Outputs: 1
print(custom_ord("c"))  # Outputs: 2
print(custom_ord("1"))  # Outputs: 26
print(custom_ord("."))  # Outputs: 36
