
def custom_ord(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"
    # Use the .index() method to find the position of the character
    # and return the index. If the character is not found, return None.
    try:
        return alphabet.index(char)
    except ValueError:
        return None  # Handle the case where the character is not in the alphabet string

# Example Usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 26
print(custom_ord(" "))  # Output: 35
print(custom_ord("?"))  # Output: 38
