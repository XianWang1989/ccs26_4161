
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    # Find the index of the character in the custom alphabet string
    index = alphabet.find(char)
    return index  # This will return -1 if the character is not found

# Example usage:
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("z"))  # Output: 25
print(custom_ord("0"))  # Output: 26
print(custom_ord("!"))  # Output: 35
