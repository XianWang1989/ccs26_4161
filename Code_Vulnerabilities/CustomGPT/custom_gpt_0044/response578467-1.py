
# Define the custom alphabet string
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Create a mapping of characters to their indices
char_to_index = {char: index for index, char in enumerate(alphabet)}

# Function to get the index of a character
def custom_ord(char):
    return char_to_index.get(char, None)  # Return None for characters not in the alphabet

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 26 (if "1" is included in your alphabet)
