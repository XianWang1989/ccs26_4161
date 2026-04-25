
def custom_ord(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"
    index = alphabet.find(char)
    if index == -1:
        raise ValueError(f"Character '{char}' not found in custom alphabet.")
    return index

# Example usage:
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord(" "))  # Output: 26 (space character)
