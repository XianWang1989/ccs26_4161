
# Define your custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Create a mapping of each character to its index
char_to_index = {char: index for index, char in enumerate(alphabet)}

# Function to get the custom ord value
def custom_ord(char):
    return char_to_index.get(char, None)  # Return None if the character is not found

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 36
print(custom_ord(" "))  # Output: 62
