
# Define your custom alphabet string
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Create a function to get the index of a character
def custom_ord(char):
    # Use the index method to find the position of the character in the alphabet
    index = alphabet.find(char)
    # Return index if character is found, else return None
    return index if index != -1 else None

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord(" "))  # Output: 36 (space character)
print(custom_ord("?"))  # Output: 43 (question mark)
print(custom_ord("Z"))  # Output: None (not in alphabet)
