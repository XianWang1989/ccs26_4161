
# Define the custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Create a function to get the custom ordinal value
def custom_ord(char):
    return alphabet.index(char)

# Examples of usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("0"))  # Output: 26
print(custom_ord(" "))  # Output: 36
