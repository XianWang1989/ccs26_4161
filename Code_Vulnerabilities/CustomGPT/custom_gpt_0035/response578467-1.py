
def custom_ord(char, alphabet):
    index = alphabet.find(char)
    return index if index != -1 else None

# Example usage
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"
print(custom_ord("a", alphabet))  # Output: 0
print(custom_ord("b", alphabet))  # Output: 1
print(custom_ord("c", alphabet))  # Output: 2
