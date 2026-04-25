
def custom_ord(char, alphabet="abcdefghijklmnopqrstuvwxyz0123456789 .,?!"):
    if char in alphabet:
        return alphabet.index(char)
    else:
        raise ValueError(f"Character '{char}' not in the custom alphabet.")

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("!"))  # Output: 36
