
# Define your custom alphabet string
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Create a function to get the custom ordinal value
def custom_ord(char):
    # Find the index of the character in the alphabet string
    index = alphabet.find(char)
    # If the character is found, return its index, else return -1 (or another indicator)
    return index if index != -1 else -1

# Test the function
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 26 (for "1" in the alphabet)
print(custom_ord("!"))  # Output: 35 (for "!" in the alphabet)
