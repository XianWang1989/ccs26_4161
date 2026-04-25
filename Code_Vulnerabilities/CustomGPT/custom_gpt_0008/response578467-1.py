
# Define your custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Create a dictionary that maps each character to its index
char_index = {char: index for index, char in enumerate(alphabet)}

# Custom ord function
def custom_ord(char):
    return char_index.get(char, -1)  # Returns -1 if the character is not found

# Usage examples
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("z"))  # Output: 25
print(custom_ord("0"))  # Output: 26
print(custom_ord("!"))  # Output: 37
print(custom_ord("x"))  # Output: 23
