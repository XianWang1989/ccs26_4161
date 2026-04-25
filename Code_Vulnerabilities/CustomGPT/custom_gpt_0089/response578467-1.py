
# Define the custom alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    # Get the index of the character in the alphabet
    index = alphabet.find(char)
    # Return the index, which will be 0 for 'a', 1 for 'b', etc.
    return index

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
