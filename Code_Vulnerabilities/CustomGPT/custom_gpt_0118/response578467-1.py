
# Define your custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Create a mapping of characters to their corresponding positions
char_to_ord = {char: index for index, char in enumerate(alphabet)}

# Example usage
print(char_to_ord['a'])  # Output: 0
print(char_to_ord['b'])  # Output: 1
print(char_to_ord['c'])  # Output: 2
print(char_to_ord['1'])  # Output: 26
print(char_to_ord[' '])  # Output: 36
