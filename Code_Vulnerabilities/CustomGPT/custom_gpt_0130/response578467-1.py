
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    index = alphabet.find(char)
    return index if index != -1 else None  # Return None for characters not in the string

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("!"))  # Output: 36
print(custom_ord("z"))  # Output: 25
print(custom_ord("1"))  # Output: 26
