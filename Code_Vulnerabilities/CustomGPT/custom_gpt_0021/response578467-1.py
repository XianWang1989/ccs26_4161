
# Define your custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Create a dictionary mapping each character to its index
char_to_index = {char: index for index, char in enumerate(alphabet)}

# Function to get the custom "ord" value
def custom_ord(character):
    return char_to_index.get(character, -1)  # Returns -1 if the character is not found

# Test the function
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 26
print(custom_ord("?"))  # Output: 34
