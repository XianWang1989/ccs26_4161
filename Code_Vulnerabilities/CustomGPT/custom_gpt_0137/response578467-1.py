
def custom_ord(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"
    # Check if the character exists in the alphabet string
    if char in alphabet:
        return alphabet.index(char)
    else:
        raise ValueError(f"{char} is not in the alphabet")

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("0"))  # Output: 26
print(custom_ord(" "))  # Output: 36
print(custom_ord("?"))  # Output: 39
