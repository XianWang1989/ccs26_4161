
# Define your custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Create a dictionary to map characters to their indices
char_to_ord = {char: index for index, char in enumerate(alphabet)}

# Define a custom ord function
def custom_ord(char):
    return char_to_ord.get(char, -1)  # Returns -1 for characters not in the alphabet

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord(" "))  # Output: 26
print(custom_ord("?"))  # Output: 36
