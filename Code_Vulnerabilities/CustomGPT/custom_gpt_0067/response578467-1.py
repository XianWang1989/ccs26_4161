
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    index = alphabet.find(char)
    return index if index != -1 else None  # Returns None for characters not in alphabet

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 26
