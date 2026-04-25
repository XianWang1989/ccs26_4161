
# Define the custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Function to get the index of a character
def custom_ord(char):
    return alphabet.index(char)

# Test the function
print(custom_ord('a'))  # Output: 0
print(custom_ord('b'))  # Output: 1
print(custom_ord('c'))  # Output: 2
