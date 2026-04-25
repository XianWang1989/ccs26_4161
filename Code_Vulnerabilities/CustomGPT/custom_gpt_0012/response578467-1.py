
# Create a custom alphabet string
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Function to get custom ordinal value
def custom_ord(char):
    # Return the index of the character in the custom alphabet
    return alphabet.index(char)

# Test examples
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("d"))  # Output: 3
