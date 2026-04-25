
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Create a mapping from characters to their index
def custom_ord(char):
    return alphabet.index(char)

# Test the custom_ord function
print(custom_ord("a"))  # Outputs: 0
print(custom_ord("b"))  # Outputs: 1
print(custom_ord("c"))  # Outputs: 2
