
def custom_ord(char):
    # Define your custom alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

    # Use the index method to get the position of the character
    index = alphabet.find(char)

    # If the character is not found, return a suitable value (e.g., -1 or None)
    if index == -1:
        return None  # or return -1

    return index

# Example usages
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("z"))  # Output: 25
print(custom_ord("1"))  # Output: 26
print(custom_ord(" "))  # Output: 32
print(custom_ord("?"))  # Output: 38
print(custom_ord("x"))  # Output: 23
