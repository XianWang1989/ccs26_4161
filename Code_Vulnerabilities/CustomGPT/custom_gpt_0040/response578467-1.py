
def custom_ord(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"
    # Find the index of the character in the alphabet string
    index = alphabet.find(char)
    if index != -1:
        return index
    else:
        raise ValueError(f"Character '{char}' is not in the custom alphabet.")

# Example usage
print(custom_ord("a"))  # Output: 0
print(custom_ord("b"))  # Output: 1
print(custom_ord("c"))  # Output: 2
print(custom_ord("1"))  # Output: 26
