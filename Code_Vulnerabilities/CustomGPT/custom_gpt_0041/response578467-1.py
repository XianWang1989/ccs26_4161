
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    # Find the index of the character in the alphabet string
    index = alphabet.find(char)
    if index == -1:
        raise ValueError(f"'{char}' is not in the defined alphabet.")
    return index

# Example usage:
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 26 (if '1' is in 'alphabet')
