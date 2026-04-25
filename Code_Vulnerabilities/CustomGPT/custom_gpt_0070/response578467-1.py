
# Define your custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Create a dictionary to map each character to its index
char_to_index = {char: index for index, char in enumerate(alphabet)}

# Define a custom ord function
def custom_ord(char):
    return char_to_index.get(char, -1)  # Return -1 for characters not in the alphabet

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("0"))  # Output: 26
print(custom_ord("!"))  # Output: 36
print(custom_ord("?"))  # Output: 37
