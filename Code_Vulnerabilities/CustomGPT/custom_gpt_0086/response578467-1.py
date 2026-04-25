
# Define your custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Function to get the index as "ord"
def custom_ord(char):
    return alphabet.index(char)

# Test the function
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("0"))  # Output: 26
print(custom_ord(" "))  # Output: 36
