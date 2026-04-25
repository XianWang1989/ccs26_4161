
# Define your custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Create a mapping of each character to its index
custom_ord = {char: index for index, char in enumerate(alphabet)}

# Function to get the custom ordinal value
def custom_ord_function(char):
    return custom_ord.get(char, -1)  # Returns -1 for characters not in the alphabet

# Example usage
print(custom_ord_function("a"))  # Output: 0
print(custom_ord_function("b"))  # Output: 1
print(custom_ord_function("c"))  # Output: 2
