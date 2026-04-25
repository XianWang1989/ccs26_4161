
def custom_ord(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"
    index = alphabet.find(char)
    if index != -1:
        return index
    else:
        raise ValueError("Character not found in alphabet")

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 26
