
# Define your custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Create a mapping from each character to its index
char_to_index = {char: index for index, char in enumerate(alphabet)}

# Now you can define a custom ord function
def custom_ord(char):
    return char_to_index.get(char, -1)  # Returns -1 for unknown characters

# Test the function
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 26 (for '0'... '9')
print(custom_ord(" "))  # Output: 36 (for space)
