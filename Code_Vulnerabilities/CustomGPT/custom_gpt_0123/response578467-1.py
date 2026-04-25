
# Define your custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Create a custom ord function
def custom_ord(char):
    if char in alphabet:
        return alphabet.index(char)
    else:
        return -1  # Return -1 for characters not in the alphabet

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 26
print(custom_ord("?"))  # Output: 35
