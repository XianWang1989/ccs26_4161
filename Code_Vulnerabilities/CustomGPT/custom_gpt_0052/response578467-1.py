
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    # Find the index of the character in the custom alphabet
    index = alphabet.find(char)
    return index if index != -1 else None  # Return None if character is not found

# Testing the function
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 26
print(custom_ord("?"))  # Output: 36
print(custom_ord("!"))  # Output: 38
