
def custom_ord(char, alphabet):
    index = alphabet.find(char)
    return index if index != -1 else None  # Return None if char is not found

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

# Example usage
print(custom_ord("a", alphabet))  # Output: 0
print(custom_ord("b", alphabet))  # Output: 1
print(custom_ord("c", alphabet))  # Output: 2
print(custom_ord("z", alphabet))  # Output: 25
print(custom_ord("0", alphabet))  # Output: 26
print(custom_ord(" ", alphabet))   # Output: 36
