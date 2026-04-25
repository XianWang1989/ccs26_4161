
# Create a string of characters
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Create a mapping from characters to their index
char_to_index = {char: index for index, char in enumerate(alphabet)}

# Define a custom ord-like function
def custom_ord(char):
    return char_to_index.get(char, -1)  # Return -1 for characters not in the alphabet

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 36
print(custom_ord(" "))  # Output: 62
