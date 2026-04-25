
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"

def custom_ord(char):
    if char in alphabet:
        return alphabet.index(char)
    else:
        return None  # or raise an error if the character is not in the alphabet

# Examples
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord(" "))  # Output: 36 (space character)
