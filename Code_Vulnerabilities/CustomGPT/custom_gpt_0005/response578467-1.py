
# Define your custom alphabet string
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Create a mapping of characters to their corresponding indices
char_to_index = {char: index for index, char in enumerate(alphabet)}

# Function to get the custom 'ord' value
def custom_ord(char):
    return char_to_index.get(char, -1)  # Return -1 if the character is not found

# Examples
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
