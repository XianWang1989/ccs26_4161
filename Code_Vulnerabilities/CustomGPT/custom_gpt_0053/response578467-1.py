
def custom_ord(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"
    # Check if the character is in the alphabet
    if char in alphabet:
        return alphabet.index(char)  # Return the index as the ordinal
    else:
        raise ValueError(f"Character '{char}' is not in the custom alphabet.")

# Example usage:
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 26
print(custom_ord(" "))  # Output: 36
