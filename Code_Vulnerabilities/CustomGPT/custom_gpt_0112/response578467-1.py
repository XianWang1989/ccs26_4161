
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Create a mapping of characters to their index
char_to_index = {char: index for index, char in enumerate(alphabet)}

# Example usage
def custom_ord(char):
    return char_to_index.get(char, None)  # Returns None if the character is not in the alphabet

# Testing the function
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("z"))  # Output: 25
print(custom_ord("1"))  # Output: 26
print(custom_ord("?"))  # Output: 36
