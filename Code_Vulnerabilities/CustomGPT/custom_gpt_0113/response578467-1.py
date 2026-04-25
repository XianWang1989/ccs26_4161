
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"
char_to_index = {char: index for index, char in enumerate(alphabet)}

# Function to get the custom ordinal
def custom_ord(char):
    return char_to_index.get(char, -1)  # Returns -1 if the character is not found

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 36
