
def custom_ord(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"
    if char in alphabet:
        return alphabet.index(char)  # Get the index of the character
    else:
        raise ValueError(f"Character '{char}' is not in the defined alphabet.")

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 26 (first digit)
