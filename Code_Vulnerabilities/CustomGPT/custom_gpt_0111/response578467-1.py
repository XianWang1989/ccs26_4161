
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Create a mapping from each character to its index
char_to_index = {char: index for index, char in enumerate(alphabet)}

# Function to get the custom index
def custom_ord(char):
    return char_to_index.get(char, -1)  # Returns -1 if the character is not found

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("z"))  # Output: 25
print(custom_ord("0"))  # Output: 26
print(custom_ord(" "))  # Output: 36
