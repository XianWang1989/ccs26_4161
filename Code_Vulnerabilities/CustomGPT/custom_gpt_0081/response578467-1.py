
# Create the custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Create a dictionary to map each character to its index
index_mapping = {char: index for index, char in enumerate(alphabet)}

# Define a function to get the custom ord value
def custom_ord(char):
    return index_mapping.get(char, None)  # Return None if the character is not found

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("0"))  # Output: 26
print(custom_ord(" "))  # Output: 36
print(custom_ord("!"))  # Output: 40
