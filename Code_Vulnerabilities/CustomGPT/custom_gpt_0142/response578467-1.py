
# Custom alphabet string
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    # Get the index using str.index() method
    try:
        return alphabet.index(char)
    except ValueError:
        return None  # Return None if the character is not found

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("z"))  # Output: 25
print(custom_ord("0"))  # Output: 26
print(custom_ord("?"))  # Output: 33
print(custom_ord("!"))  # Output: None (since "!" is not in the alphabet)
