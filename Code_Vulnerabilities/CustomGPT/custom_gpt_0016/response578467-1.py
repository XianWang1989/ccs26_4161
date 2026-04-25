
def custom_ord(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"
    # Check if the character is in the string
    if char in alphabet:
        return alphabet.index(char)
    else:
        raise ValueError("Character not in the custom alphabet")

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 26 (if "1" is included in your custom alphabet)
print(custom_ord(" "))  # Output: 35 (spaces, punctuation and other characters according to your custom string)
